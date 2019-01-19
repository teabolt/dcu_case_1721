; Add two numbers read from the simple keyboard. The result is displayed on the 7 segment display
; If the result is length one, the right side is used
; If the result is length two, both sides are used

JMP main



ORG 10 ; 7 segment display value table for hex numbers 0-F (right side based)
DB FB ; 0	; address 10
DB 0B ; 1
DB B7 ; 2
DB 9F ; 3
DB 4F ; 4
DB DD ; 5
DB FD ; 6
DB 8B ; 7
DB FF ; 8
DB CF ; 9	; address 19
DB EF ; A	; address 1A
DB 7D ; B
DB F1 ; C
DB 3F ; D
DB F5 ; E
DB E5 ; F	; address 1F



ORG 20	; 'HEX_VALUE' procedure for converting an ASCII code for a hex digit into an actual hex value
; Parameters: AL, the code
; Returns: AL, the value
; Do nothing if the code is out of range of hex digit codes (0-9 and lowercase a-f)
	; Check ranges - invalid, decimal, hex
	CMP AL, 30
	JS val_end	; AL < 30 (invalid)
	CMP AL, 3A
	JS val_dec	; AL < 3A (is a 0-9 code)
	CMP AL, 61
	JS val_end	; AL < 61 (invalid)
	CMP AL, 67
	JS val_hex 	; AL < 67 (is a A-F code)
	JMP val_end	; (invalid)

	val_hex: ; code is between 'a' and 'f' (lowercase)
		SUB AL, 57	; value found experimentally
		JMP val_end
	val_dec:	; code is between '0' and '9'
		SUB AL, 30
	val_end:
		RET



ORG 40	; procedure 'SPLIT', splits a number into its most and least significant digits
; Parameters: AL, the number
; Returns: AL as the MSD, BL as the LSD
	PUSH AL	; copy AL to BL
	POP BL
	; MSD
	AND AL, F0	; mask on the second byte
	DIV AL, 10	; shift the second byte onto the first byte
	; LSD
	AND BL, 0F	; mask on the first byte
	RET



ORG 50	; procedure '7SEG_VALUE', gets the value for a digit from the 7 segment display table
; Parameters: AL, the digit
; Returns: AL, the 7seg value
	ADD AL, 10	; offset+start=index
	MOV AL, [AL]	; get the actual value
	RET



ORG 70	; MAIN program entrance point
main:
	CLO
	; pre-clear the 7seg
	MOV AL, 00
	OUT 02	; left side
	INC AL
	OUT 02	; right side
	MOV BL, 2	; decreasing loop
	readloop:
		IN 00	; read a digit
		CALL 20	; get the digit's value
		PUSH AL ; save the value
		DEC BL	; 1 iteration done
		JNZ readloop	; if haven't reached zero yet, go on
	POP BL	; 2nd digit
	POP AL	; 1st digit
	ADD AL, BL ; get the result

	CALL 40	; split the digit into MSD(AL) and LSD(BL)
	; branch based on if the answer is one or two digits wide
	CMP AL, 0
	JZ one_wide ; the MSD is 0 (it's just there for padding - the answer is one wide)

	; two_wide
	; MSD
	CALL 50 ; get the value for the MSD
	DEC AL	; display on the left
	OUT 02
	; LSD
	PUSH BL ; copy BL onto the AL
	POP AL
	CALL 50	; get the value for the LSD
	OUT 02	; display the value (right side)
	JMP terminate

	one_wide:
		PUSH BL ; copy BL onto the AL
		POP AL
		CALL 50	; get the value for the LSD
		OUT 02	; display the value (right side)

	terminate:
		HALT	; stop the CPU


END	; end of source code