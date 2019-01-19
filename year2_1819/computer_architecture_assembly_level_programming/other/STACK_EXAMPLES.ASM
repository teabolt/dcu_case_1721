MOV AL, 2
JMP mid

ORG 7F
mid:
	JMP start

ORG C0
start:
	POP BL
	JMP start
END