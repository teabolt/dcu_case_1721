; Print the alphabet A to Z on the VDU
; Implement with a loop

; ASCII codes
; A: 41
; Z: 5A

; (Assembly-time solution:)
;ORG C0
;DB "abcdefghijklmnopqrstuvwxyz"
;ORG 0
;END

; (Execution-time solution)
CLO
MOV AL, 41		; starting character to be printed
MOV CL, C0		; starting point of VDU
MOV BL, 1A		; number of iterations for loop
alphabet:
	MOV [CL], AL	; print
	INC AL		; next character
	INC CL		; next VDU position
	DEC BL		; one iteration gone
	JNZ alphabet
END