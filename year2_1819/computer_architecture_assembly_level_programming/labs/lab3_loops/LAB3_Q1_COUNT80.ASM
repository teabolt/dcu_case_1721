; Count from 8 to 0 (both inclusive) in the CL register

CLO
MOV CL, 8		; initialise register
count:			; label for loop
	DEC CL		; decrement
	JNZ count	; repeat if zero condition not met
END			; have reached zero