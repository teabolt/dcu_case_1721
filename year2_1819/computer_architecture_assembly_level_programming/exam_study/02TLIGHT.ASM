; Control the traffic lights realistically
; Relevant ports: 01 - traffic lights (write-only)
; There will be inaccuracies if the CPU is not fast enough

JMP main	; jump over the IVT
DB 10	; interrupt timer 0x02



ORG 10	; ISR 'TIME', writes the current time in 'ticks' (number of seconds) to [B0] memory location
	; in the configuration tab set how much '1' tick is equal 
	; (set it to 1 second for realistic results)
	CLI	; don't take any more ticks (CPU must be fast enough for accurate results)

	MOV BL, [B0] ; get current tick count
	INC BL       ; increment and save the tick count
	MOV [B0], BL

	IRET


ORG 20	; procedure 'CLEAR', turns off the traffic lights
	; no back ups
	MOV AL, 00
	OUT 01
	RET



ORG 30	; procedure 'CYCLE', iterates through the LIGHT SEQUENCE table once
	; not doing any backups
	MOV CL, C0	; table pointer
	cycle_loop:	; a 'do-while' loop (table must have at least 1 entry)		
		MOV AL, [CL]	; traffic lights value
		OUT 01		; display the value
		CALL 50		; block until the required amount of seconds pass
		INC CL		; next table entry
		MOV AL, [CL]	; get value
		CMP AL, 02	; compare to table terminator
		JNZ cycle_loop	; to next iteration if not at the end
	RET



ORG 50 ; procedure 'BLOCK_LIGHTS' waits until a certain time is reached 
	; before letting the next light be switched to
; Parameters: CL (current table pointer)
	PUSH AL		; back up used registers
	
	PUSH CL		; copy CL to DL
	POP DL	
	ADD DL, 10	; add offset for contiguous table
	MOV DL, [DL]	; get table value

	MOV BL, [B0]	; get current count
	ADD DL, BL	; get required count
	block_loop:
		STI	; enable timer interrupts
		MOV BL, [B0]	; check count
		CMP BL, DL	; if non equal, continue
		JNZ block_loop

	POP AL		; restore used registers
	RET


ORG 70
main:
	CALL 20	; reset the traffic lights
	loop:
		CALL 30	; step through a sequence of the traffic lights
		JMP loop
	; no need for 'HALT' as the program ends automatically upon hitting 00 in RAM



ORG B0	; 'known' memory locations
DB 00	; initialise 'ticks' count (non-global)



ORG C0	; LIGHT SEQUENCE table (using space of memory mapped VDU)
DB 24	; green, 0010_0100
DB 48	; yellow, 0100_1000
DB 90	; red, 1001_0000	
DB 02	; table terminator



ORG D0	; LIGHT TIMER table, contiguous to LIGHT SEQUENCE table
	; tells the number of seconds a traffic light should stay on
DB 14	; green : 20 seconds
DB 03	; yellow: 3 seconds
DB 0A	; red: 10 seconds
; no table terminator needed (this table corresponds to the LIGHT SEQUENCE table)



END