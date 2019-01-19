; Recursive factorial procedure, using the stack for parameter passing
; Overflows fast (or overrides the 'IP stack'

MOV CL, 9F	; CL is a global pointer for a second 'IP' stack (do not override this register)
		; the second stack starts from 9F and goes downwards (eg: AE, AD, AC, ...)
		; points to the currently free location
		; CL+1 contains the last value

; main program
MOV AL, 1
loop:
	PUSH AL		; N
	CALL 60
	POP BL		; N!
	PUSH AL		; AL -> DL
	POP DL
	ADD DL, BF	; BF+offset
	MOV [DL], BL	; show output (memory mapped VDU ignored)
	INC AL
	JMP loop



ORG 20	; procedure 'IP_PUSH', pushes a value to the IP stack
; Parameters: DL (the value), CL (global, IP stack pointer)
; Returns: modified CL pointer
	MOV [CL], DL
	DEC CL
	RET



ORG 30	; procedure 'IP_POP', pops a value off the IP stack
; Parameters: CL (global, IP stack pointer)
; Returns: DL (the popped value), modified CL pointer 
	PUSH AL

	PUSH CL
	POP AL

	INC AL
	MOV DL, [AL]
	INC CL
	
	POP AL
	RET



ORG 60	; procedure 'REC_FAC', computes the factorial of a number recursively
	; N! = N*(N-1)*(N-2)*...*2*1
; Parameters: 
	; top of stack (the number N whose factorial is to be computed, N > 0)
	; (global) IP stack pointer (CL)
; Returns: top of stack (resulting factorial N!)
; Destroys: BL, DL
	; input
	POP DL		; retrieve the PC off the stack (get access to stack parameters)
	CALL 20		; back up the current IP
	POP BL		; get N
	; back up used registers
	PUSH AL	

	; base case
	CMP BL, 1
	JZ fac_end	

	; recursive case	
	PUSH BL		; make a copy of BL on the stack
	DEC BL		; get N-1
	PUSH BL		; put the argument on top of the stack
	CALL 60		; get the factorial value (result on top of stack)
	POP AL		; (N-1)!	
	POP BL		; N
	MUL BL, AL	; N*(N-1)! = N!
	
	fac_end:
		; restore used registers
		POP AL		
		; output
		PUSH BL		; N! on top of stack
		CALL 30		; get the saved IP off the IP stack
		PUSH DL
		RET		; pops off the IP



END