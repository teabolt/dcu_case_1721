; Command Line Interface

; IVT
JMP cli_main
DB 0F		; 0x02 (timer, disabled)
DB 20		; 0x03 (keyboard, most work)

ORG 0F		; a do-nothing general interrupt block
IRET

; CLI program entrance point
ORG 10
cli_main:
	CLO		; close unwanted windows
	STI		; enable interrupts
	MOV CL, C0	; VDU pointer, points to a currently free cell
	OUT 07		; display the interrupt keyboard
	repl:
		JMP repl


ORG 20	; keyboard, process entered character
	CLI		; disable further interrupts
	IN 07		; character in AL
	CMP AL, 0D	; enter
	JZ kbi_enter
	CMP AL, 08	; backspace
	JZ kbi_backspace


	; Character handlers
	kbi_display:	; display the character on the VDU
		MOV [CL], AL
		INC CL
		JZ kbi_reset_cursor	; if cursor overflow
		JMP kbi_end

	kbi_enter:	; put the cursor at the start of a newline and execute the line entered
		AND CL, F0	; reset to start
		ADD CL, 10	; go to next line
		CMP CL, 0	; check if cursor is overflown from hitting enter
		JZ kbi_moveup	; move up the cursor and the lines
		JMP kbi_end
		
	kbi_backspace:	; delete the previous character and go to the left with the cursor
			; does nothing if already at the start of the VDU
		CMP CL, C0
		JZ kbi_end

		DEC CL
		MOV DL, 20
		MOV [CL], DL	; whitespace
		JMP kbi_end


	; Helper routines

	kbi_reset_cursor:
		MOV CL, C0
		JMP kbi_end

	kbi_moveup:	
		MOV CL, F0	; move the cursor to the start of the last line
		CALL 80		; move up the line

	kbi_end:
		STI
		IRET


ORG 60	; clear the current line
; Input: CL (line to be cleared - C0, D0, E0, or F0)
	PUSH CL		; back up the input
	PUSH DL
	PUSH BL

	MOV BL, 10	; initialise offset
	clear_loop:	; downwards loop
		DEC BL
		ADD BL, CL	; get index
		MOV DL, 20
		MOV [BL], DL	; whitespace
		SUB BL, CL	; restore starting point
		
		JNZ clear_loop
	
	POP BL	
	POP DL
	POP CL	; restore the VDU pointer
	RET



ORG 80	; shift up the current lines, freeing up the last line
	PUSH CL
	PUSH DL
	PUSH BL
	
	MOV DL, D0		; cell to be copied *from* (source)
	move_block:
		MOV BL, [DL]	; get copy
		SUB DL, 10	; cell to be copied *to* (destination)	
		MOV [DL], BL	; do copy
		ADD DL, 10	; restore source
		INC DL
		CMP DL, 00	; check if at the end (overflown)
		JNZ move_block

	MOV CL, F0	; clear the last line	
	CALL 60

	POP BL
	POP DL
	POP CL
	RET

;#pypre include mod.ASM

END