; Read a string on the VDU and print the number of times each vowel occurs in the string.
; Implementation: Contiguous vowel and count array & VDU read with clear

; Register uses:
; AL - pointer to vowels/counters, CL - pointer to VDU locations, BL/DL - temporary/general

ORG C0
DB "hellou worlde"
DB 0				; null character to indicate end of string

ORG 0				; gap for program data, address 02 to 0F
JMP start
DB "aeiou"			; the "data array"
DB 0				; counts for each vowel
DB 0
DB 0
DB 0
DB 0

ORG 10				; program code begins
start:
	MOV CL, C0		; pointer to start of VDU
prune:				; read each string character
	MOV BL, [CL]		; character at VDU
	MOV AL, 02		; pointer to vowel character & vowel count, reset each iteration
	vowel:
		MOV DL, [AL]		; character at data array
		CMP BL, DL		; matching character
		JZ count
		; next vowel iteration
		INC AL
		CMP AL, 07
		JNZ vowel
	; next prune iteration
	MOV DL, [CL]		; temporary save of current character
	MOV BL, 20		; overwrite with empty space
	MOV [CL], BL		
	CMP DL, 0		; if character was null
	JZ display		; to next phase
	INC CL
	JMP prune		; not null, go to next iteration
count:				; (current character can not be null)
	ADD AL, 05		; get to the counters of data array
	MOV DL, [AL]		; copy current count
	INC DL			; increment the count
	MOV [AL], DL		; write back the new count
	; next prune iteration
	MOV BL, 20
	MOV [CL], BL
	INC CL			
	JMP prune
display:
	MOV CL, C0		; reset VDU pointer
	MOV AL, 02		; reset pointer at vowels and counts
	frequency:		; "frequency display" loop
		MOV BL, [AL]		; character at data array
		MOV [CL], BL

		INC CL			; colon ':' character
		MOV BL, 3A
		MOV [CL], BL		

		INC CL			; frequency value at data array
		PUSH AL			; temporary save to not lose track of a vowel
		POP DL
		ADD DL, 05		; get to count in data array
		MOV BL, [DL]		
		ADD BL, 30		; get ascii character of number - only works for 0 to 9
		MOV [CL], BL
		ADD CL, 02		; skip for a space

		; to next "frequency display"
		INC AL					
		CMP AL, 07		; check if at the end
		JNZ frequency
	JMP terminate
terminate:
	END
