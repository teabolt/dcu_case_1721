; Playing around with interrupts
; 2) Use the keyboard hardware interrupts

; Interrupt Vector Table begins
JMP main ; jump over
DB 1F	 ; skip over timer interrupt 
; timer interrupt problem:
; go to ISR that does nothing - solution to it messing things up
; way to disable the timer device??? Set it to a high number?
DB 50    ; advanced keyboard interrupt vector
DB 70	 ; advanced keypad interrupt vector; map both to same ISR? - need different port handling



ORG 20
main:	; main program
	CLO		; close unwanted windows
	MOV AL, 0	; init AL (counter of keypresses)
	MOV CL, C0	; init CL (position of free VDU cell)
	loop:	; infinite loop to keep the program runnning for testing purposes
		STI	; enable interrupts
		;OUT 07	; force display the keyboard (shows even if close - infinite loop)
		OUT 08	; display a numeric keypad
		; both work together???
		JMP loop



ORG 1F	; timer interrupt
IRET	; do nothing



ORG 50 ; keyboard ISR
CLI	; stop handling other keypresses
; case: get some 'lag', stack overflows / overrides code
; case against: not as responsive, still 'lag'
; need to wait until finish with ISR to enter another character
INC AL ; add one each time the interrupt happens
PUSH AL	; backup
IN 07	; get the ASCII character pressed
MOV [CL], AL
INC CL
; global modified
; not parametrizing -> don't know when will be called / not like a procedure?
JNZ exit
reset:
	MOV CL, C0
exit:
POP AL	; restore original AL (incremented - 'global' like?)
IRET
; can write out characters very easily (user-friendly) !!!
; bug - CL will overflow from FF to 00 -> will start overriding - override IVT -> dif. interrupt code - probably will stop running
; fix - 'cycle' CL



ORG 70 ; numeric keypad ISR
CLI
IN 08	; read the character
MOV [CL], AL
INC CL
IRET


END