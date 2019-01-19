; Read one character from the keyboard and split its two digit ASCII code
; Split the digit using bitwise operators (mask with AND)

IN 00		; read the character (results in a byte in AL)

PUSH AL		; copy AL to not lose it
PUSH AL
POP BL		; first digit
POP CL		; second digit

AND BL, F0	; F0 = 0b1111_0000 (keep first 4, zero the rest)
DIV BL, 10	; divide by 10 (16) to move digit to left

AND CL, 0F	; 0F = 0b0000_1111 (zero the first 4, keep the rest)

END