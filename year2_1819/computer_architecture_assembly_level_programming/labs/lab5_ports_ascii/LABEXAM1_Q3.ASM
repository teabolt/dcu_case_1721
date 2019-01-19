; LAB EXAM 1 Q3 REVIEW

; Calculator for two digits (0 to 9), supporting +, -, *, and /, with a VDU display.
; Relevant ASCII codes:
; 0-9: 30-39, A-F: 41-46
; = 3D
; + 2B, - 2D, * 2A, / 2F

; VDU structure:
; C0 - first digit, C1 - operator, C2 - second digit, C3 - equals sign,
; C4 - first result digit, C5 - second result digit


; Set up for applying the operator, this reduces memory usage significantly

; Store possible operations in an array of memory
; OPERATION - OPCODE - ASCII CODE
; ADD - A0 - 2B
; SUB - A1 - 2D
; MUL - A2 - 2A
; DIV - A3 - 2F
; Register AL - 00, register BL - 01

; Use the fact that the opcodes of arithmetic operators ADD, SUB, MUL and DIV are \
; contiguous from A0 to A3
ORG A0
; set up for linear search
DB 2B	; store the ASCII value of the operator symbol at the 'opcode address'
DB 2D
DB 2A
DB 2F
; special code, addresses A4 to A8, to carry out the operation
; (literary writing the program in DB's)
do_operation:		; label to jump to later	
	DB 0		; a dummy space for an arithmetic operator's opcode
	DB 0		; register AL, where result will be stored
	DB 1		; register BL
	JMP result	; jump back to the correct place

; Observe: jumps take up memory, but labels don't take up memory

ORG 0		; Start of the program
CLO
MOV BL, 80	; set up a stack terminator (extrema of negative numbers, -128; zero could be used in the program)
PUSH BL		

; Enter all input: 1st digit, operator, 2nd digit
; No validation is done, as there may not be enough memory for all the checks
MOV BL, 3	; loop variable
MOV CL, C0	; VDU pointer
readall:	; loop to read AND print what was read
	IN 0	; keyboard result (ASCII char), stored in AL
	MOV [CL], AL
	INC CL	; go to next VDU location
	DEC BL	; to next iteration
	JNZ readall

; Add an equals sign
MOV BL, 3D
MOV [CL], BL
INC CL

; Convert digit characters to values
MOV CL, C0	; reset VDU pointer
MOV AL, [CL]	; first digit
convert_digs:
	SUB AL, 30	; make a code value into an arithmetic value
	PUSH AL		; store value on the stack
	ADD CL, 2	; go in increments of two
	MOV AL, [CL]	; get next digit (if valid loop)
	CMP CL, C4	; jump if haven't reached 4 (1 too far)
	JNZ convert_digs
; Stack results from the top: second digit, first digit

; Do the calculation
; Carry out an operation (will be messing with opcodes in RAM and stuff)
MOV CL, [C1]	; the operator's ASCII code
MOV DL, 9F	; position variable (reference ORG A0 set up done at the start of the program) 
; (one less for start)
; Linear search on the array of possible operations and their ASCII values defined in the beginning
lsearch_op:
	INC DL		; to next character
	MOV BL, [DL]	; get the ASCII value at the RAM position
	CMP CL, BL	; compare if values match
	JNZ lsearch_op	; not the right operator, go on
	; done
; DL holds the opcode value of the correct operator
MOV [A4], DL	; load the operator
; put the right values in the right registers
POP BL		; second digit
POP AL		; first digit
JMP do_operation	; do the calculation (result stored in AL)

result:			; label that do_operation will jump back to
; Convert result value to digit characters
PUSH AL		; AL will be the first digit
POP BL		; BL will be the second digit
MOD BL, 10	; get the least significant digit only
SUB AL, BL	; get the most significant digit only
DIV AL, 10	; shift the M.S. digit to the left

; store the results on a stack
PUSH BL
PUSH AL
; Stack results from top: first digit, second digit

POP DL ; at the start: second digit
MOV CL, C4		; VDU pointer initialised to the correct position
printloop:		; go through each result digit, printing it on the VDU ('do-while' loop)
	; check if the digit is 0-9 or A-F (due to different conversion to ASCII character codes)
	CMP DL, A	; DL < A
	JS to_digit
	JNS to_letter	; A <= DL
	to_digit:
		ADD DL, 30
		JMP print
	to_letter:
		ADD DL, 37
	print:
		MOV [CL], DL
	INC CL
	POP DL
	CMP DL, 80	; check if not at stack end
	JNZ printloop

END

; Extra's:
; More operators supported - MOD, DEC, INC
; Support negative numbers (negative subtraction). Re-order the numbers and put a '-'/sign before them?
; Validate user input
; Clear the VDU before the program begins