; Implement a Queue
; A single register, AL, acts as the Queue pointer

; queue from BL (inclusive) and CL (exclusive)
MOV BL, A0
MOV CL, AF

PUSH BL
POP AL  	; start of queue

MOV BL, 80
MOV [CL], BL	; queue terminator

MOV BL, 30	; value to be addded
loop:
CALL 50		; enqueue
JMP loop


ORG 50
; 'enqueue' procedure
; uses value in BL
MOV [AL], BL
INC AL	; new empty space
RET

ORG 60
; 'dequeue' procedure
; stores the result in BL
DEC AL	; go back
MOV BL, [AL]
RET


END