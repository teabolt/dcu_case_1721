; ===== ARITHMETIC AND REGISTERS ======================================
	CLO		; Close unwanted windows.
	MOV AL, ff
	MOV BL, 1
	MOV CL, 7
	MOV DL, 8
	ADD BL, AL
	ADD CL, BL
	ADD DL, CL
	END		; Program ends
; ===== Program Ends ===========================================

	YOUR TASK
	=========
	Use SUB, DIV and MUL to subtract, divide and multiply.
	What happens if you divide by zero?
	Make use of CL and DL as well as AL and BL.
