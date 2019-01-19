; Count down using the seven segment display from 99 to 00 (use both digits)
; every second (timer interrupt)
; configuration -> set hardware timer interval to 1 second

; Relevant device info:
; Hardware timer is at 0x02 of IVT
; 7-segment display is write-only at port 02


JMP main	; jump over the IVT
DB 20		; address of ISR for the hardware timer
DB 0
DB 0
DB 1F		; software interrupt 0x05, terminate program (jumps to 00/empty value)

ORG 10		; 7 segment display numbers table ('left side' form)
DB FA ; 0	; at position 10
DB 0A ; 1
DB B6 ; 2
DB 9E ; 3
DB 4E ; 4
DB DC ; 5
DB FC ; 6
DB 8A ; 7
DB FE ; 8
DB CE ; 9	; at position 19

ORG 70                                                                       
main:	; start the actual program
	CLO	; close undesirable windows
	CALL 60	; clear the 7-segment display
	MOV BL, 19	; 7-segment left side pointer
	MOV CL, 19	; 7-segment right side pointer
	MOV AL, [BL]	; initial lights
	OUT 02
	MOV AL, [CL]
	INC AL
	OUT 02
	loop:
		STI	; enable hardware interrupts (everything ready to handle them)
		JMP loop
	HALT	; a useless HALT?


ORG 20	; 'hardware timer' ISR
; use the interrupt as a 'loop'
; modifying 'globals' BL and CL
CLI	; don't handle any more interrupts
PUSH AL	; back up used register
; check if left hand digit is not out of bounds
CMP BL, 10
JS exit_program	; BL < 10
; not out of bounds, keep going
DEC CL	; go to next number
CMP CL, 10	; check if in bounds
JS left_counter	; not in bounds (CL < 10), change the left digit
right_counter:	; in bounds, update the right digit
	MOV AL, [CL]
	INC AL
	OUT 02	; send the new number to the display
	JMP exit_timer
left_counter:
	DEC BL		; get the next left side digit
	CMP BL, 10	; check if in bounds
	JS exit_timer	; not in bounds
	; in bounds
	MOV AL, [BL]	; set the right side
	OUT 02
	MOV CL, 19	; reset the right side
	MOV AL, [CL]
	INC AL
	OUT 02
exit_timer:
	POP AL	; restore backed up register
	IRET	; get back to where were before
exit_program:
	INT 05	; a software interrupt without a return
; fix: stop decrementing when go out of bounds with left digit pointer
; alternatively break out of the main infinite loop
; done: change both digits (when required) in one go of the interrupt
; stats: behind like 19 seconds


ORG 60	; procedure 'CLEAR_7SEG'
PUSH AL	; backup used register
MOV AL, 00	; turn off the left side
OUT 02
INC AL		; turn off the right side
OUT 02
POP AL	; restore register
RET


END