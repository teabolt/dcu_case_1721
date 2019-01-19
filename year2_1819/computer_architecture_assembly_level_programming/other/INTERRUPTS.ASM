; Playing around interrupts (stopping and doing something else - need to run not step)
; 1) Add one to AL each time a second passes

JMP main	; jump over the Interrupt Vector Table (starts at 00, stores addresses of interrupt code)
DB 50		; 0x02 -> timer interrupt -> is at location dropped (a callback like thing/procedure)


ORG 20		; main program
main:
	MOV AL, 0	; initialise time counter
	; ignore interrupts so far
	loop:		; keep on executing the program
		STI	; enable interrupt handling (sets I flag / to value 10) (each time)
		; case for enabling it each time in the loop 
		; - when the ISR is entered interrupt handling is disabled
		; IRET DOES NOT enable it (SMS detail), so need to re-enable it yourself
		; INT 02 ; artifically call the interrupt via software (doesn't matter if it's CLI or STI)
		JMP loop

ORG 50
; timer interrupt handler (interrupt service routine)
; a hardware interrupt (external)
CLI	; ignore other interrupts (sets flag to 0) 
; Case for using CLI:
; if don't use it and CPU is slow, will just be handling interrupts all day
; however time will be more accurate?
; BUT stack will eventually overflow
INC AL
IRET	; return to where were before in execution (pop IP)

; timing the effectiveness of the timer with a stopwatch - largely depends on the CPU speed
; eg: dispatch latency! (instructions to increment the AL)
; but if the CPU is set to maximum speed, then it's close to actual stopwatch time
; handling interrupts when an interrupt has occured improves accuracy at lower CPU speeds
; but at some point when the CPU is very slow, it's just entrance into interrupts
; illustrates fundamental timing problem???
; better to handle timing in software? Use a hardware timer just for 'calibration'?

END