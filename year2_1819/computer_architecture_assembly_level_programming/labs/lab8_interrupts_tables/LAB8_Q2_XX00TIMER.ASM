; Countdown timer from the number entered via the advanced keyboard
; Relevant devices:
; 7 segment display: PORT 02
; Timer hardware interrupt: 0x02
; Advanced keyboard interrupt: 0x03, PORT 07

JMP main	; jump over the IVT
DB 20		; timer vector
DB 30		; keyboard vector


ORG 10	; 7 segment display number table (right-side based)
	DB FB	; 0	; at position 10
	DB 0B	; 1
	DB B7	; 2
	DB 9F	; 3
	DB 4F	; 4
	DB DD	; 5
	DB FD	; 6
	DB 8B 	; 7
	DB FF	; 8
	DB CF	; 9	; at position 19


ORG 20	; timer ISR - count each second
	; uses BL and CL for the MSB and LSB of the 'DTUPLE' structure
	CLI	; don't take more interrupts
	CALL 8A	; display the digits
	CALL 70 ; get the next digits
	IRET
	

ORG 30	; advanced keyboard ISR - enter two digits
	; This modifies DL!!!
	IN 07
	CMP AL, 30	
	JS kb_end	; AL < 30
	CMP AL, 39	
	JNS kb_end	; AL >= 3A
	POP DL	; save the previously saved IP
	PUSH AL	; save digit
	INC BL	; increase digit count
	CMP BL, 2
	JZ setup_dtuple
	kb_end:
		PUSH DL
		IRET
	

ORG 50
main:	
	CLO	; close unwanted windows
	CALL AA ; clear the 7seg
	; Use a 'digit tuple' (own invented) data structure
	; The structure is of the form (a, b), where a and b are between 0 and 9
	; Essentially this represents a two-digit decimal number
	; initialise starting values - take from the advanced keyboard
	OUT 07	; force display of the advanced keyboard
	MOV BL, 0	; keep track of how many digits were read
	readloop:	; read until get two digits
		;CLI	; disable interrupts (so that the timer doesn't mess things up)
		INT 03	; call the advanced keyboard ISR in software (keep on polling)
		JMP readloop
	setup_dtuple:
		POP CL	; LSB
		SUB CL, 30	; turn from ASCII codes into arithmetic values
		POP BL	; MSB
		SUB BL, 30
	loop:		; infinite runtime loop
		STI	; enable interrupts for the timer
		JMP loop
	HALT	; stop the CPU

ORG 70	; procedure DTUPLE DECREMENT - subtract one from the 'digit tuple' data structure
	; handling overflows appropriately
; Parameters: BL - The MSB, CL - The LSB
; Returns: Modified BL and CL
	DEC CL	; decrease the LSB
	; check if overflow
	JS dec_msb	; overflown, decrease MSB (CL < 0)	
	RET	 	; no overflow, done

	dec_msb:
		DEC BL		; decrease the MSB
		; check if MSB has overflown
		JS dec_base	; overflown (BL < 0) 
	MOV CL, 9	; no overflow, reset value of LSB to maximum
	RET

	dec_base:
		MOV BL, 0	; set both digits to 0
		MOV CL, 0
		RET


ORG 8A	; procedure DISPLAY DTUPLE - show each digit on the 7 segment display 
	; (assume a table exists)
; Parameters: BL as the MSB, CL as the LSB
	PUSH AL	; back up used register
	; MSB
	MOV AL, 10	; index of number = starting point + offset
	ADD AL, BL
	MOV AL, [AL]	; get the 7seg value
	DEC AL	; set to the left side
	OUT 02
	; LSB
	MOV AL, 10
	ADD AL, CL
	MOV AL, [AL]
	OUT 02
	POP AL ; restore back up
	RET


ORG AA	; procedure CLEAR - clear the 7 segment display
	PUSH AL	; back up used register
	MOV AL, 00	; clear the left
	OUT 02
	MOV AL, 01	; clear the right
	OUT 02
	POP AL	; restore backed-up register
	RET
	

END