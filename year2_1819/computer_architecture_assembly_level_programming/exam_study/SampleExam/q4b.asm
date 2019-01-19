; This is a replica of the file used in the real exam.
; if you are sending me code in answer to questions on the  sample paper, *do not* include any of the information requested here.

; six-digit exam number		17350793
; seat number (if available)	17

;code goes below this point.


; Minimum
; Program for finding numeric minimums over data sets



; main (tests)
	CLO
	MOV AL, A0	; set array bounds for test data
	MOV BL, A9
	CALL 30		; find the minimum number in the array
	MOV [C0], AL	; display the result (will be a raw hex value)
	HALT



ORG 20
; procedure MIN, identifies the smaller of two numbers (REUSED FROM Q4A.ASM)
; Input: AL (first number), BL (second number)
; Output: AL (the smaller of the two numbers)
	CMP AL, BL	; S set if AL < BL
	JS end_min	; AL is the minimum
	; else BL is the minimum / numbers are equal
	PUSH BL
	POP AL

	end_min:
		RET



ORG 30
; procedure MINIMUM, determines the smallest number in an array
; Input: AL (array start address), BL (array end address) (both inclusive, assume non-empty)
; Output: AL (the minimum number)
; Uses the MIN procedure
	PUSH CL		; make backups
	PUSH BL

	MOV CL, [AL]	; initial guess
	INC AL		; onto the next number

	INC BL		; make the loop bound check work (turn inclusive into exclusive)
	; a 'while' loop
	condition:
		; main minimum logic
		PUSH BL		; back up the upper bound
		PUSH AL		; back up current number pointer

		MOV BL, [AL]	; get the current number being checked (number two)
		PUSH CL		; get the current guess (number one)
		POP AL
		CALL 20		; the bigger of AL and BL is stored in AL
		PUSH AL		; move the updated guess into CL
		POP CL
		; note that this updates CL even if there is no need for an update

		POP AL		; restore current number pointer
		POP BL		; restore the upper bound

		CMP AL, BL	; Z set if AL = BL (at the exclusive end)
		JZ min_end
	min_iter:
		INC AL
		JMP condition
	min_end:
		PUSH CL		; copy CL to AL (answer)
		POP AL

		POP BL		; restore backups
		POP CL
		RET



ORG A0	; test data (9 hex numbers)
	DB 05
	DB 03
	DB 03
	DB 00
	DB FF
	DB 7F
	DB 80
	DB 81
	DB 30
	DB 25



END