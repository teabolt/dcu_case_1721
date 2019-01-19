; Read a hexadecimal byte number from the keyboard
; Not a general solution but specialised for a byte hexadecimal (8 bits, 2 characters wide)
; According to the register widths

; Assuming conversions to negative and positive numbers are handled by the assembler / simulator
; Support only for uppercase hex digits, eg: 'A', not 'a'
; <TO-DO>: lowercase support

; Relevant ASCII codes (character to hexadecimal map)
; 0: 30, 1: 31, 2: 32, 3: 33, 4: 34, 5: 35, 6: 36, 7: 37, 8: 38, 9: 39
; A: 41, B: 42, C: 43, D: 44, E: 45, F: 46
; (CAPS LOCK REQUIRED)


CLO
MOV DL, 0
PUSH DL 			; null value for stack end (sentinel)

; Read two characters
IN 0				; read the first character
PUSH AL				; store MSB in stack
IN 0				; read the second character
PUSH AL				; store LSB in stack



; Translate each ASCII character code to actual hex values

; Digits 0 to 9: maths equation with range check (simpler maths)
; Digits A to F: contiguous array map		 (like 1 more instruction, but anyways...)

MOV DL, 2			; get two iterations
MOV CL, A0 			; store values in RAM (A0 and A1 - need to change - LSB then MSB)
loop:
POP AL				; get a digit
; check "ranges" that the digit falls into
digit_range:				; "decimal" range 0-9, ASCII ranges 29 to 40 exclusive
	MOV BL, 29			; lower bound
	CMP BL, AL			; BL is less than AL
	JNS terminate			; number is not too small, mismatch - no point in checking the next range (has a higher upper range anyways - short circuit)
	MOV BL, 40			; upper bound
	CMP AL, BL			; AL is less than BL
	JNS letter_range		; number is not too big. go to next range to be checked
	JMP digit_process 		; number is in range


letter_range:				; "letter" range A-F, ASCII ranges 40 to 47 exclusive
	MOV BL, 40			; lower bound
	CMP BL, AL
	JNS terminate
	MOV BL, 47			; upper bound
	CMP AL, BL
	JNS terminate
	JMP letter_process		; the number is in this range

digit_process: 				; processing digits 0-9
	SUB AL, 30				; constant offset formula
	JMP condition				; next

letter_process:				; processing "letters" A-F
	SUB AL, 41			; map (complicating things with DB, RAM, etc) vs constant offset formula (harmonious)
	ADD AL, 0A
	JMP condition

condition:				; loop condition
	MOV [CL], AL
	INC CL
	DEC DL
	CMP DL, 0
	JNZ loop
	JMP calculate

	

; calculate the actual number
; in byte case (2 hex characters): MSB*10+LSB
calculate:
	MOV CL,	[A1]	; MSB 
	MOV DL,	[A0]	; LSB
	PUSH CL		; result=MSB*10+LSB
	POP AL
	MUL AL, 10
	ADD AL, DL
terminate:
	END