; Program to interact with the VDU

; Initial pointer set
JMP start
; Do not modify this space. Go to label 'start' instead

; Data (addresses 02 to 2F inclusive) and directives
;DB 11		; DC1 - device control 1, used here to force letters to be lowercase
DB "hello"	; stores bytes of ascii chars
DB 0A		; LF - new line feed
DB "there"
DB 0D		; CR - carriage return, go to start of line
DB "0200141718819?"
DB 0		; NUL - end of string
ORG 30		; move program, allocate space for data

; Processing
start:
	CLO		; close unwanted windows
	MOV AL, 02	; start of data to write
	MOV BL, C0	; start of VDU memory mapped locations
	JMP loop	; proceed write

loop:
	MOV CL, [AL]	; get the current ascii byte
	; check if special character
	CMP CL, 0	; NUL (end of string)
	JZ end
	CMP CL, 0A	; \n (new line)
	JZ newline
	CMP CL, 0D	; \r (carriage return) (known bug - additionally goes to the next line)
	JZ carriage
	; assuming valid "graphical" or "printable" characters
	MOV [BL], CL	; write character
	INC BL		; move to next screen location
	INC AL		; move to next character

	JMP loop

newline:
	ADD BL, 10 	; go to next line, cx -> dx -> ex -> fx.
	INC AL		; go to next character
	JMP loop	; get back into writing

carriage:
	;MOV DL, BL	; temporary save
	PUSH BL
	POP DL
	MOD DL, 10	; get remainder of '0xAB' as 'B'
	SUB BL, DL	; set '0xAB' to '0xA0'
	INC AL
	JMP loop

end:
	END