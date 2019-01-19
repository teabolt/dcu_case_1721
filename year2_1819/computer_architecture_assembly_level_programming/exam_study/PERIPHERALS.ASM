; SMS peripherals


JMP main


ORG 10	; snake and maze controls table (contains the snake control code and how many times it should be repeated)
DB 4F 	; DOWN
DB 0B
DB 1F	; RIGHT
DB 03
DB 8F	; UP
DB 05
DB 1F	; RIGHT
DB 03
DB 4F 	; DOWN
DB 05
DB 1F	; RIGHT
DB 02
DB 8F	; UP
DB 08
DB 2F	; LEFT
DB 05
DB 8F	; UP
DB 03
DB 1F	; RIGHT
DB 07
DB 4F 	; DOWN
DB 0B
DB FF 	; STOP


ORG 30		; solve the maze and snake
	MOV AL, FF	; reset the maze
	OUT 04
	MOV BL, 10	; initialise controls table pointer
	JMP condition
	control_snake:
		INC BL
		MOV CL, [BL]
		command_loop:
			OUT 04
			DEC CL
			JNZ command_loop
		INC BL
	condition:
		MOV AL, [BL]
		CMP AL, FF
		JNZ control_snake
	RET


ORG 50	; table for stepper motor
DB 00
DB 01
DB 02
DB 04
DB 08

DB 03
DB 06
DB 0C
DB F0 	; END

ORG 70
main:
	CLO
	; CALL 30	; Snake and Maze
	;MOV AL, 01
	;OUT 06
	;IN 06
	motor:
	MOV BL, 50
	motor_loop:
		OUT 05
		INC BL
		MOV AL, [BL]
		CMP AL, F0
		JNZ motor_loop
	JMP motor
	HALT


END