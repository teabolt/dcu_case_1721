; Queue implemented with a circular buffer
; Barebones program (not many parametrisations)



MOV BL, 0 ; dequeue pointer (offset)
MOV CL, 0 ; enqueue pointer (offset)
MOV AL, 15
enq_loop:
	CALL 40
	DEC AL
	JNZ enq_loop
PUSH CL
MOV CL, F0
deq_loop:
	CALL 70
	MOV [CL], AL
	INC CL
	CMP CL, F5
	JNZ deq_loop
POP CL
MOV AL, 55
enq_loop2:
	CALL 40
	DEC AL
	CMP AL, 50
	JNZ enq_loop2
HALT



ORG 40	; ENQUEUE  procedure, enqueues an item
; Input: AL (item)
; Error: DL = FF (queue is full / can not override)
	MOV DL, [CA]	; item count
	CMP DL, 0A	; only allow 10 items
	JZ full

	enq:
		ADD CL, C0	; get to beginning of queue array
		MOV [CL], AL
		SUB CL, C0	; restore the pointer as an offset only
		INC CL		; point to next possibly free location
		MOD CL, 0A	; circle around the buffer
		INC DL		; increase item count
		MOV [CA], DL	
		JMP end_enq

	full:
		MOV DL, FF
	
	end_enq:
		RET




ORG 70	; DEQUEUE procedure, dequeues an item
; Output: AL (item dequeued)
; Error: DL = FF (empty / no item to dequeue)
	MOV DL, [CA]
	CMP DL, 0
	JZ empty

	deq:
		ADD BL, C0	; item
		MOV AL, [BL]
		SUB BL, C0
		INC BL		; pointer
		MOD BL, 0A
		DEC DL		; item count
		MOV [CA], DL
		JMP end_deq

	empty:
		MOV DL, FF

	end_deq:
		RET



; Queue data
ORG C0	; data array (C0 to C9)

ORG CA	; number of items (metadata)
DB 0



END