; This is a replica of the file used in the real exam.
; if you are sending me code in answer to questions on the  sample paper, *do not* include any of the information requested here.

; six-digit exam number		17350793
; seat number (if available)	17

;code goes below this point.



JMP main	; jump over the IVT
DB 0A		; 0x02 - hardware timer, initially not used, afterwards handles waits/timing
DB 0A		; 0x03 - keyboard, not used
DB 10		; 0x04 - numeric keypad, handles keypresses


ORG 0A	; general purpose 'do nothing' ISR
IRET


ORG 10	; keypad ISR, validates and stores a keypress
; Uses parameters: BL (lowest allowable value), CL (highest allowable value) (both in ASCII)
; Affects: DL is incremented (represents count of keypresses)
; Destroys: AL (reads the keypress value AND leaves it there)
	CLI	; stop further presses
	PUSHF	; save the flags

	IN 08		; read the key press (store in AL)
	PUSH DL		; back up keypress counter
	CALL 80		; validate the keypress
	CMP DL, FF	; check if valid
	JZ kp_err	; invalid keypress, don't save
	; valid keypress
	POP DL
	INC DL	; increase keypress count
	JMP kp_end

	kp_err:		; ignore invalid keypress
		POP DL

	kp_end:
		POPF	; enable flags
		STI	; enable new keypresses
		IRET


ORG 28		; timer ISR, handles waits (modifies the time counter)
; Affects: CL (time counter)
	PUSHF	; back up flags	(just in case)
	CLI	; stop further interrupts
	DEC CL	; modify the time counter
	STI	; enable further interrupts
	POPF	; restore flags
	IRET




ORG 30	; main code
main:
	CLO		; close unwanted windows
	CALL A0		; pre-clear the 7 segment display
	OUT 08		; show the keypad (done once, do not close)
	MOV DL, 0	; initialise keypress counter
	MOV BL, 30	; lower exclusive keypress bound
	MOV CL, 39	; upper exclusive keypress bound
	STI		; enable interrupts
	read_val:
		CMP DL, 1	; AL < DL, at least one key press should be read
		JNZ read_val
	CLI
	; valid value in AL
	SUB AL, 30	; 'normalise' the value, from ASCII to hex value
	PUSH AL		; save the value

	MOV BL, 30	; update upper and lower bounds
	MOV CL, 3A	; include 9
	STI
	read_iter:	; read the iteration count
		CMP DL, 2
		JNZ read_iter
	CLI
	; count in AL
	SUB AL, 30	; normalise
	
	; set up to display the digit
	PUSH AL		; number of iterations in BL
	POP BL
	POP AL		; number to be shown in AL
	MOV CL, 28	; modify the hardware timer IVT to be used as a wait mechanism
	MOV [02], CL	
	; (reference Q5b for implementing a wait procedure - some of the code is used here)
	show_number:	; downwards loop to display the digit a number of times
		CALL 90		; display the value on the 7 segment display
		; wait for one second (assume that the hardware timer is set to one second)
		MOV CL, 1	; initialise second counter
		STI	; enable interrupts
		wait_loop:
			CMP CL, 0	; stop condition
			JNZ wait_loop	; keep going or stop
		CLI	; stop interrupts
		CALL A0		; clear the 7seg display
		DEC BL		; 1 iteration done
		JNZ show_number
	HALT



ORG 80	; procedure VALIDATE_BOUNDS, checks if a value is in bounds
; Input: AL (value), BL (lower bound), CL (upper bound) (both exclusive)
; Error: DL = FF (AL not in bounds)
	CMP BL, AL	; BL < AL
	JNS valid_err
	CMP AL, CL	; AL < CL
	JNS valid_err
	JMP valid_end

	valid_err:
		MOV DL, FF
	valid_end:
		RET		



ORG 90	; procedure 7SEG_DISPLAY, displays a single digit on the right side of the 7 segment display
	; uses the 7 segment display table
	; digits 0 to 9 accepted
; Input: AL (the value to be displayed)
	PUSH AL

	ADD AL, C0
	MOV AL, [AL]
	OUT 02

	POP AL
	RET



ORG A0	; procedure 7SEG_CLEAR, clears the 7 segment display, both sides
	PUSH AL

	MOV AL, 00
	OUT 02
	INC AL
	OUT 02

	POP AL
	RET
	


ORG C0	; 7SEGMENT DISPLAY TABLE (overrides the memory mapped VDU)
	; right side
	; 0 to 9
DB FB	; 0
DB 0B	; 1
DB B7	; 2
DB 9F	; 3
DB 4F 	; 4
DB DD	; 5
DB FD	; 6
DB 8B	; 7
DB FF	; 8
DB CF	; 9



END