; Flash a cursor on the VDU
; Relevant ASCII codes:
; space - 20
; _	- 5F (not displaying on the VDU, bug? -> use a dash(-) of 2D instead)
; or 49 (I)

JMP main
DB 70

ORG 40
main:
	STI
	loop:
		INT 02
		JMP loop


ORG 70
; timer interrupt
CLI
MOV AL, [C0]
CMP AL, 20
JNZ notclear
; clear
MOV BL, 49
MOV [C0], BL
JMP endi
notclear:
	MOV BL, 20
	MOV [C0], BL
endi:
	IRET

END