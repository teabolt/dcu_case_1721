; Test more complex keyboard reads, print to VDU, LED

CLO
MOV DL, 0
PUSH DL 			; null value for stack end (sentinel)

; Read an arbitrary amount of any characters
; 'do-while' and 'while' constructs
input:				; read characters until user hits 'enter'
	IN 0			; wait for a key press from the keyboard
	PUSH AL			; store characters on the stack (including final 'enter')
	CMP AL, 0D		; check if user hit 'enter' (carriage return character)
	JNZ input		; read another key press	
	; set up and go to the next stage
	POP BL			; throw away the last 'enter' character
	MOV CL, C0		; pointer to a VDU location, starting at the first cell
	JMP print

print:				; print each character entered in reverse, excluding the final 'enter'
	POP BL			; the character
	CMP BL, 0		; check if reached end of stack
	JZ terminate		; go to the next stage
	MOV [CL], BL		; write character to the VDU
	INC CL			; go to the next VDU location
	JMP print		; go to next iteration
terminate:
	MOV DL, 0		; move sentinel back
	PUSH DL			
	END