; Procedure 'print', displays a character stored in [31] 
; on a VDU location stored in [30] (memory)


CLO	; close unwanted windows

; test
MOV AL, C0	; ! at top left
MOV BL, 21
CALL 60
CALL 70

MOV AL, D0	; 0 at second row left
MOV BL, 30
CALL 60
CALL 70

MOV AL, FF	; ~ at right bottom
MOV BL, 7E
CALL 60
CALL 70

HALT


; procedure 'set print args'
; moves values from AL and BL to memory locations [30] and [31] resp.
ORG 60
MOV [30], AL
MOV [31], BL
RET


; procedure 'print' - display a character on the VDU
; parametrised over VDU locations and character to print, using memory [30] and [31] resp.
ORG 70
MOV CL, [30]	; get VDU location
MOV BL, [31]	; get character
MOV [CL], BL	; print the character
RET

END	; end of source