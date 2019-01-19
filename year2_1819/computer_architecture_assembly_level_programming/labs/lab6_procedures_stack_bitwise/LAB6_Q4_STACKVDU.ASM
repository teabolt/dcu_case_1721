; Procedure 'print' displays a character on the display
; Parametrised via a stack

CLO
;  test 
MOV AL, C0	; ^ to top left
MOV BL, 5E
PUSH AL
PUSH BL
CALL 70
MOV AL, E7	; # to 3rd row middle
MOV BL, 23	
PUSH AL
PUSH BL
CALL 70
HALT


; procedure 'print', displays a character on a VDU point
; has arguments 'position' (where to print on the VDU), 'character' (which character to print)
; arguments passed by the stack - push position, then push the character
; registers _ are backed up *via memory from location A0*
ORG 70
; back up registers
MOV [A0], AL
MOV [A1], BL
MOV [A2], CL
MOV [A3], DL
; do the print
POP CL	; previous address of IP
POP BL	; character
POP AL	; position
MOV [AL], BL	; print
PUSH CL	; restore IP address
; restore registers
MOV AL, [A0]
MOV BL, [A1]
MOV CL, [A2]
MOV DL, [A3]
RET

END