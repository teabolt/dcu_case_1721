; Put an uppercase string onto the VDU at assembly-time.
; Replace each instance of a vowel in the string with an instance of 'Z' at execution-time.

; ASCII codes
; A - 41
; E - 45
; I - 49
; O - 4F
; U - 55

; Z - 5A

JMP start			; set IP to point at start of code
DB "aeiou"			; store for vowels, addresses 02 to 2F		

ORG C0				; assembly-time VDU store
DB "hey oh under about integer!?	 aeiou zzzxxxyyy"

ORG 30				; store for code
start:
	CLO
	MOV CL, C0		; VDU position and outer loop variable

scan:			; increasing loop
	MOV BL, [CL]		; temporary save
	MOV AL, 02		; vowel pointer, reset each time before inner loop
	vowel:		; increasing innner loop
		MOV BL, [AL]	; temporary save for vowel value
		MOV DL, [CL]	; temporary save for VDU character value
		CMP DL, BL
		JZ replace
		INC AL		; move to the next vowel
		CMP AL, 07	; check if not out of range
		JNZ vowel
	; go to next VDU location
	INC CL
	JNZ scan
	; reached end of VDU
	JMP terminate

replace:		; routine for replacement with Z
	MOV BL, 5A		; temporary save of Z value
	MOV [CL], BL		; replace with Z
	; go to next
	INC CL
	JNZ scan
	; reached end of VDU
	JMP terminate

terminate:
	END