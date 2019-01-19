; Control the patterns of the traffic lights with bitwise operators

CLO

start:
JMP race

disco:			; one light on, rest on
MOV AL, 80		; 1000_0000
disco_loop:
	XOR AL, FF	; 1111_1111
	OUT 01
	JMP disco_loop
; Make the single light change each time?

one_two:		; one traffic on, another traffic on
MOV AL, E0		; 1110_00XX (EO) -> 0001_11XX (1C)
one_two_loop:
	XOR AL, FF
	OUT 01
	JMP one_two_loop

sequence:		; green -> yellow -> red -> ...
MOV AL, 20
sequence_loop:
	OUT 01
	ROL AL ; 0010_0000 (20) -> 0100_0000 (40) -> 1000_0000 (80) -> 0000_0001 -> ...
	JMP sequence_loop

race:			; light up at the same time
MOV AL, 24
MOV DL, 3
race_loop:
	OUT 01		; 0010_0100 (24) -> 0100_1000 -(48) > 1001_0000 (90)
	SHL AL
	DEC DL
	CMP DL, 0
	JZ race
	JMP race_loop
; Use modulo, or some other bitwise operator?

terminate:
	END