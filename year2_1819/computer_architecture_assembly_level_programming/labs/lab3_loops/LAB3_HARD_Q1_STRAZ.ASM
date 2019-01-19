; Put an uppercase string onto the VDU at assembly-time.
; Replace each instance of 'A' in the string with an instance of 'Z' at execution-time.

; ASCII codes
; A - 41
; Z - 5A

ORG C0
DB "advanced assembly and an ants artwork arnold amy arp ads"

ORG 0
CLO
MOV CL, C0		; position and loop variable
scan:
	MOV BL, [CL]	; temporary save
	CMP BL, 41	; if A
	JZ replace
	; go to next
	INC CL		; next position
	JNZ scan
	; reached end of VDU
	JMP terminate
replace:
	MOV BL, 5A	; temporary move
	MOV [CL], BL	; replace with Z
	; go to next
	INC CL
	JNZ scan
	; reached end of VDU
	JMP terminate
terminate:
	END