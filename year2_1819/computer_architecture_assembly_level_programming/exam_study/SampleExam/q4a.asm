; This is a replica of the file used in the real exam.
; if you are sending me code in answer to questions on the  sample paper, *do not* include any of the information requested here.

; six-digit exam number		17350793
; seat number (if available)	17

;code goes below this point.


; Minimum
; Progrem implementing numeric minimum routines for pairs of numbers



; main code (tests)
	CLO
	MOV AL, 05	; two test numbers
	MOV BL, 06
	CALL 20		; print the smaller of the two
	HALT



ORG 20	; procedure MINP, prints the smaller of two numbers on the VDU
; Input: AL (first number), BL (second number)
; Output: VDU cell [C0] contains the smaller of the numbers (in numeric ASCII form)
	CALL 30	; get the smaller of AL and BL to AL
	CALL 50	; convert the number if possible
	MOV [C0], AL	; displays the digit (or just the hex value if no conversion was possible)
	RET



ORG 30	; procedure MIN, identifies the smaller of two numbers
; Input: AL (first number), BL (second number)
; Output: AL (the smaller of the two numbers)
	CMP AL, BL	; S set if AL < BL
	JS end_min	; AL is the minimum
	; else BL is the minimum / numbers are equal
	PUSH BL
	POP AL

	end_min:
		RET
		


ORG 50	; procedure TO_DIG, converts a single digit hex 0-9 value to its numeric ASCII counterpart
; Input: AL (hex value)
; Output: AL (ASCII value)
; Error: leaves AL unmodified (not a hex number in range 0-9)
	PUSH BL

	; check lower bound (FF)
	MOV BL, FF
	CMP BL, AL	; BL < AL
	JNS end_dig
	; check upper bound (0A)
	CMP AL, 0A 	; AL < 0A
	JNS end_dig
	; in bounds, convert
	ADD AL, 30

	end_dig:
		POP BL
		RET



END