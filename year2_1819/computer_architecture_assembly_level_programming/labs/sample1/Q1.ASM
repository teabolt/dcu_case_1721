; Put a string on the VDU (any case) (assembly-time), 
; and reverse the case of all its letters (run-time),
; (lowercase -> uppercase, uppercase -> lowercase)

; Relevant ASCII codes:
; Uppercase letters A-Z: 41-5A
; Lowercase letters a-z: 61-7A

ORG C0			; start of VDU
; string: I LOVE asSEmblY
DB "I love "		; by default, the assembler makes the entire string uppercase (I LOVE)
DB 61			; "a"
DB 73			; "s"
DB "S"
DB "E"
DB 6D			; "m"
DB 62			; "b"
DB 6C			; "l"
DB "Y"
DB 0			; null terminator for end of string

ORG 0			; code
; CMP A, B sets the S flag if A < B

; loop through each letter until hit null ('while' loop construct)

; initialisation
MOV CL, C0		; pointer at a VDU location, starts at first cell
MOV AL, [CL]		; first character at a VDU location

condition:
	CMP AL, 0	; check if character is not null
	JNZ loop	; if not at end of string
	JMP terminate	; finished, end the program

loop:			; body of the loop
; Detect whether the character is lowercase/uppercase, do a corresponding uppercase/lowercase transform
is_upper:			; uppercase character falls into range 40 to 5B, exclusive
	; lower bound
	MOV BL, 40
	CMP BL, AL		; 40 is smaller than the character code
	JNS next		; character too small, out of any bounds
	; upper bound
	MOV BL, 5B
	CMP AL, BL		; character code is smaller than 5B
	JNS is_lower		; character too big, but might be lowercase
	JMP to_lower		; character is uppercase, make it lowercase

is_lower:			; lowercase character falls into range 60 to 7B, exclusive
	; lower bound
	MOV BL, 60
	CMP BL, AL
	JNS next		; character code too small (but too big to be uppercase)
	; upper bound
	MOV BL, 7B
	CMP AL, BL
	JNS next		; character code too big
	JMP to_upper		; character is lowercase, make it uppercase	

; Uppercase and lowercase letter ASCII codes differ by a constant (20) 
; Upper to lower: +20
to_lower:
	ADD AL, 20
	MOV [CL], AL		; replace the current character with its tranformed version
	JMP next

; Lower to upper: -20
to_upper:
	SUB AL, 20
	MOV [CL], AL
	JMP next


next:	; set up for next iteration
	INC CL		; next VDU cell
	MOV AL,	[CL]	; character at cell
	JMP condition

terminate:
	END