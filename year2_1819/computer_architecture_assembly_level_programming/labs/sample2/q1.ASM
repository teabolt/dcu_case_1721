; Fill the VDU with alternating 0's and 1's every second
; Stop at the end

; Use the timer interrupt (0x02 -> set it to one second in the configuration tab)


JMP main	; jump over the IVT
DB 10		; hardware timer interrupt 0x02
DB 00		; skip over 0x03
DB 00		; skip over 0x04
DB 40		; software interrupt 0x05

ORG 10	; timer interrupt displays a 1 or a 0 in a VDU cell 
	; and prepares for the next iteration
; Parameters: BL (currrent value), CL (current VDU location)
; Returns: New BL and CL OR exits the program
	CLI	; don't take any more interrupts
	PUSH AL	; back up used registers
	PUSH DL

	MOV [CL], BL	; display the current value
	INC CL	; go to the next free cell
	JZ terminate	; CL has overflown (became 0)
	; no overflow, get the next value for BL
	; use bitwise manipulation
	PUSH BL		; copy BL into DL
	POP DL
	AND DL, 01	; only keep the last bit in CL
	XOR DL, 01	; flip the last bit in CL
	AND BL, FE	; discard the last bit in BL
	ADD BL, DL	; fuse BL and CL

	POP DL	; restore used registers
	POP AL
	IRET
terminate:	; case when CL has reached the end of the VDU
	INT 05  ; call a software interrupt


ORG 40	; stop the program
	HALT


ORG 70	; the main program body
main:
	CLO		; close unwanted windows
	; initialise values
	MOV CL, C0	; the VDU pointer
	MOV BL, 30	; ASCII code for 0
	loop:		; main runtime loop
		STI	; listen for interrupts
		JMP loop	
	

END