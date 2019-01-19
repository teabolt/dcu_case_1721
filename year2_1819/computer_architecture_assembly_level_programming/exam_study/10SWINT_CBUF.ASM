; Circular buffer implementation
; 'deque' data structure (two-end queue)



; 'main' of the program
; make a new deque
MOV AL, B0
MOV BL, C7
MOV CL, 3
CALL 20
; add an item on the right
MOV BL, 10
loop_enq:
	CALL 90
	DEC BL
	JNZ loop_enq
loop_deq:
	CALL 60
	JMP loop_deq
HALT


; DEQUE data structure
; Variables
	; Left pointer (point to currently free locations)
	; Right pointer
	; Current size
	; Maximum size
	; Data array start pointer
; Subroutines
	; Constructor
	; Append left
	; Append right
	; Pop left
	; Pop right


ORG 20
; procedure 'NEW_DEQUE', creates a new empty deque with all attributes initialised
; Input: 
;	- AL (metadata pointer - where deque's attribute data begins to be stored),
;	- BL (data array pointer - where the deque's actual data begins to be stored, could grow in either direction),
;	- CL (max size - maximum size of the deque data array,
;		0 for unlimited, >0 for circular
; Output: AL (deque reference - pointer to all that is needed to act on the deque, do not lose!)
	PUSH AL		; this will be the deque reference
	PUSH DL		; backup used register

	MOV [AL], BL	; initialise left pointer
	INC AL
	MOV [AL], BL	; initialise right pointer
	INC AL
	MOV DL, 0
	MOV [AL], DL	; initalise current size of deque
	INC AL
	MOV [AL], CL	; set maximum size of deque
	INC AL
	MOV [AL], BL	; set starting point of deque data array

	POP DL		; restore used register
	POP AL		; restore deque reference
	RET


; All the following methods pass the deque reference in AL

ORG 50
; procedure 'ENQUEUE_LEFT'
NOP


ORG 60
; procedure 'DEQUEUE_RIGHT'
; removes an item from the right of the deque
; Output: CL (the item removed) (Error code: FF if the deque is empty)
	PUSH AL
	PUSH DL

	; check the current size
	INC AL		; get current size
	MOV DL, [AL]
	CMP DL, 0
	JZ dr_empty
	
	DEC DL		; decrease the size
	MOV [AL], DL
	DEC AL		; get the right pointer
	MOV DL, [AL]
	DEC DL		; decrement the pointer
	MOV CL, [DL]	; get the item
	MOV [AL], DL	; save new pointer value
	JMP dr_end

	dr_empty:
		MOV CL, FF
	
	dr_end:
	POP DL
	POP AL
	RET


ORG 90
; procedure 'ENQUEUE_RIGHT'
; adds an item to the right of the deque
; Input: BL (the item to be enqueued)
	PUSH AL		; back up deque reference
	PUSH CL		; general back up

	INC AL		; get the right pointer
	MOV CL, [AL]
	MOV [CL], BL	; enqueue the item
	INC CL		; update the right pointer
	MOV [AL], CL
	INC AL		; get current size
	MOV CL, [AL]
	INC CL		; increase the size
	MOV [AL], CL	

	POP CL ; general restore
	POP AL ; restore deque reference
	RET


; ORG 90
; procedure 'DEQUEUE_LEFT'
; NOP


END