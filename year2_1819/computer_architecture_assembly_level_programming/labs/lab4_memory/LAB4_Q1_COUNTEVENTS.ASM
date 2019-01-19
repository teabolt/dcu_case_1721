; Count the number of odd numbers in the entire RAM
; The result will go into AL

; test sequences
ORG 40
; positive numbers
DB 3
DB 5
DB 7
DB 8
DB A	; 10
DB 7F	; 127
DB 7E	; 126

ORG 50
; numbers less than or equal to divisor
DB 0
DB 1
DB 1
DB 2

ORG 60
; negative numbers
DB 80	; -128
DB 81	; -127
DB 82	; -126
DB FF	; -1
DB FE	; -2

; code - it is included in the count itself
ORG 00
MOV CL, 00		; initialise pointer to RAM location
MOV AL, 00		; initialise count of odd numbers
loop:			; loop through each memory location (a 'do-while' construct)
	MOV BL, [CL]	; save value at current RAM location
	MOD BL, 2 	; if number is odd, it has a non-zero remainder after division by two
	JNZ count	; jump if odd (zero flag not set)
	condition:	; onto next iteration
		INC CL
		CMP CL, 00	; if checked all memory locations (overflown from FF to 00)
		JNZ loop
		JMP terminate
count:		; increment counter variable and return to loop (an 'if' construct)
	INC AL
	JMP condition	; jump back to condition
terminate:
	END