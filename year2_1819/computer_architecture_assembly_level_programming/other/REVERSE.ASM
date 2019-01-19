; Reverse a string that has been put on the VDU at assembly-time
; Implemented with a stack
; String and stack terminators are put back where they belong in the final exit of the program

ORG C0				; start of memory mapped VDU
DB "hello world 123 navan"		; string
DB 0				; null terminator for end of string

ORG 0				; start of code
; copy the string to the stack
MOV CL, C0			; initialise pointer at a VDU memory location
MOV BL, FF			; temporary save
PUSH BL				; mark end of stack

JMP condition
store:				; store the string on the VDU to the stack
	MOV AL, [CL]		; get the character at the VDU cell
	PUSH AL			; store the character on the stack
	INC CL			; next VDU cell
condition:
	MOV BL, [CL]
	CMP BL, 0		; check if at the end of string
	JNZ store
	; next step

MOV CL, C0			; reset VDU pointer
rewrite:			; write the string in reverse
	POP AL			; get a character
	CMP AL, FF		; check if not end of stack
	JZ terminate		; exit if at the end
	MOV [CL], AL
	INC CL
	JMP rewrite

terminate:
	MOV BL, FF
	PUSH BL			; write-back the stack terminator
	END