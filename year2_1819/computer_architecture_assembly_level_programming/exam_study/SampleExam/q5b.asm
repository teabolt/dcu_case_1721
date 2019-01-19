; This is a replica of the file used in the real exam.
; if you are sending me code in answer to questions on the  sample paper, *do not* include any of the information requested here.

; six-digit exam number		17350793
; seat number (if available)	17

;code goes below this point.


; Explicit waits
; Program implementing a wait procedure that blocks execution of the program for a specific number of seconds,
; using the hardware timer.

; It is assumed that the hardware timer fires an interrupt every second.
; It is also assumed that the CPU is fast enough so that the timer ISR can execute in a second.
; (the faster the CPU, the greater the accuraccy)



JMP main 	; jump over the IVT
DB 40		; 0x02 - hardware timer



ORG 20
main:		; main code (tests)
	CLO		; close unwanted windows
	MOV AL, 5	; wait for 5 seconds
	CALL 60	
	MOV DL, 5	; do something, wait, do something
	MOV AL, FF
	CALL 60
	DEC DL
	HALT		; stop execution
	


ORG 40		; the timer ISR, decrements AL once (signifies a second passing)
	CLI	; stop further interrupts
	DEC AL
	STI	; re-enable interrupts
	IRET
	; this is not a general purpose ISR. It is tied closely to the WAIT procedure.
	; if you enable interrupts to use this timer on its own, I am not responsible for what happens to you



ORG 60		; procedure WAIT, blocks/delays the program for a number of seconds
; Input: AL (number of seconds)
; The procedure enables interupts for its runtime and disables them upon exit
	PUSH AL ; back up used register

	STI	; take timer interrupts
	wait_loop:
		CMP AL, 0
		JNZ wait_loop

	CLI	; disable timer interupts
	POP AL 	; restore used register
	RET



END		; end source