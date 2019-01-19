; Control the heater and thermostat

CLO
MOV DL, 0		; time instant, upper limit of 7A (to keep arithmetic consistent)
MOV CL, 0		; acts as a flag of the heater's state (on - 1, off - 0)
initialise:		; heater off for start
	MOV AL, 00
	OUT 03

reset_timer:
	MOV DL, 0
time:
	; introduces delays to queries, query every 10 instants
	PUSH DL
	POP BL
	MOD BL, 1	; can be very responsive (1), average (A), or very unresponsive (7A)
	JZ query
	; night time - turn off the heater
	; to-do check if heater not off already AND it's night time
	;CMP DL, 60
	;JNS turn_off 	; 60 <= DL
time_cond:
	INC DL
	CMP DL, 80
	JZ reset_timer
	JMP time

query:
	IN 03
	PUSH AL		; backup copy
	XOR AL, CL	; 1-1 act off, *0-0 act on*, 1-0 leave, 0-1 leave (either thermostat high or heater on)
	JZ do_action
	POP AL		; clear copy
	JMP time_cond	

do_action:
	; temp high (heater off), temp low (heater on)
	POP AL	; restore copy
	CMP AL, 0
	JZ turn_on ; temperature low
	; temperature high
	MOV BL, 1	; use a delay when turning off
	JNZ turn_off
	
turn_on:
	MOV AL, 80
	OUT 03
	INC CL
	JMP time

turn_off:
	CMP BL, 1	; control flag register set to 1
	JNZ off 	; not set, go without a timer
	off_delay: ; wait for 40(hex) instants to let the water heat extra
	PUSH DL
	POP BL
	ADD BL, 40
	off_delay_loop:		
		INC DL		
		CMP DL, BL
		JS off_delay	; DL < BL
	off:
	MOV AL, 00
	OUT 03
	DEC CL
	JMP time_cond


END
