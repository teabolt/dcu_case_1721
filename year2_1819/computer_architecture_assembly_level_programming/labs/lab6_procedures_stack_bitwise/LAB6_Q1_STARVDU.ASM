; Procedure 'print', displays a star * on a VDU location stored in [30] (memory)
; Relevant ASCII codes:
; * = 2A


CLO	; close unwanted windows

; test
MOV AL, C0	; star at top left
MOV [30], AL
CALL 70
MOV AL, FF	; star at bottom right
MOV [30], AL
CALL 70
HALT

; procedure 'print'
; parametrised over VDU locations, using memory
ORG 70
MOV CL, [30]	; get VDU location
MOV BL, 2A	; get asterisk
MOV [CL], BL
RET

END	; end of source