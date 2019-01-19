; Download Bar in the VDU (between D0 and DF)

JMP main
DB 30	; 0x02, hardware timer


ORG 10		; entrance point
main:
	CLO	; close unwanted windows
	; display bar borders
	MOV AL, 5B	; [
	MOV [D0], AL
	MOV AL, 5D	; ]
	MOV [DF], AL
	MOV BL, 0	; progress (offset)
	STI		
	dl_loop:	; begin the download
		CMP BL, 0E
		JNZ dl_loop

	

ORG 30		; timer ISR, a download of a block happens each second
	INC BL
	CALL 50
	IRET



ORG 50		; procedure PROGRESS_BAR, reflects the progress of the offset in the VDU
; Input: BL (current progress offset)
; Output: VDU write
	PUSH AL
	ADD BL, D0	; add starting point
	MOV AL, 2A	; a star * representing a bar in a progress indicator
	MOV [BL], AL	
	SUB BL, D0	; remove starting point
	POP AL
	RET



END