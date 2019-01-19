; Watchdog Timer for a simulated Mars Rover

JMP main
; IVT
DB A0	; 0x02 hardware timer - enable the Monitor via the timer hardware
DB 30	; 0x03 advanced keyboard - enable surroundings read
DB A0	; 0x04 key pad - enable heat state read

ORG A0	; generic ISR 'do nothing'
IRET


ORG 10
main:			; execution starting point for the Rover software
	CLO		; close previously used interfaces
	CALL 20		; start the communications hub

	; Communications Hub calls
	
	; Watchdog Timer / Monitor calls



ORG 20	; procedure RUN_COMMS, starts an execution loop for the communications hub
	OUT 07		; take input from surroundings
	MOV BL, 0	; initialise network card buffer pointer
	STI		; continually read environment data
	env_read_loop:
		JMP env_read_loop



ORG 30	; ISR for environment input, passes the data to the network interface buffer
; Uses: BL (current free buffer location)
; Destroys: AL (reads the data)
	IN 07		; save the data
	ADD BL, C0	; add offset to the network card
	MOV [BL], AL	; write out the data
	SUB BL, C0	; remove the offset
	INC BL		; onto the next buffer location
	MOD BL, 41	; make the buffer circular (0x40 is the maximum size of the network card buffer)
	IRET
	


; RUN_MONITOR

; CHECK_WATCHDOGFLAG

; BITE


; RUN_HEATCONTROL


END