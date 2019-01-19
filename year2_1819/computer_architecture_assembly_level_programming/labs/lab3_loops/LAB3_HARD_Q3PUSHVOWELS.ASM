; Display a (uppercase) string at assembly-time
; At run-time, collect all the vowels from the VDU onto the stack

ORG C0			; start of memory mapped VDU
DB "hello world united init exit vwlss aeiou"
DB 0	; null character, end of string

ORG 0
CLO
MOV AL, C0		; pointer at a VDU cell
loop:
	MOV BL, [AL]	; value at cell
	CMP BL, 0
	JZ exit		; reached end of string, terminate
	; check if character is *any* vowel
	CMP BL, 41	; A
	JZ vowel
	CMP BL, 45	; E
	JZ vowel
	CMP BL, 49	; I
	JZ vowel
	CMP BL, 4F	; O
	JZ vowel
	CMP BL, 55	; U
	JZ vowel
	; if any comparison results in zero, character is a vowel
	; repeated jumps, since only the last operation is considered
	; can kind of "short-circuit" based on which ever vowel is most frequent

	; no vowels found
	; next iteration
	INC AL		; next character
	JMP loop
vowel:
	MOV BL, [AL] 		; temporary storage
	PUSH BL			; collect vowel onto the stack
	; next iteration
	INC AL
	JMP loop
exit:
	END
	
MOV AL, C0		; reset pointer to start of VDU
clear:
	MOV BL, 20		; temporary save for empty space (assuming that's the "blank" character)
	MOV [AL], BL		; set cell to empty space
	MOV BL, [AL]		; temporary save
	INC AL			; next cell
	MOV BL, [AL]	
	CMP BL, 0		; repeat until null character (assuming nothing was written after null)
	JNZ clear
	; reached null char - reset it too
	MOV BL, 20
	MOV [AL], BL