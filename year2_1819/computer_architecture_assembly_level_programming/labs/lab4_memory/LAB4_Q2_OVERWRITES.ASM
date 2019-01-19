; Program that overwrites itself
; Implementation without a stack PUSH

MOV AL, BF		; initialise AL to act as a stack pointer
MOV BL, FF		; number to overwrite the program with
loop:
	MOV [AL], BL
	DEC AL
	JMP loop
END

; This only overwrites the first byte of the program, eg: the 'loop' part of 'JMP loop'
; Then the program stops (does not crash).
; Explanation:
; 'JMP loop' becomes 'JMP FF' (overwrite last byte).
; IP points to 'JMP FF', CPU executes the command. (it so happens with the IP)
; Hypothesis: JMP <address> adds IP's current value and <address>
; FF is -1. Thus, a jump is made to the just preceding address.
; IP points  to 'AL', CPU attempts to execute the "command".
; The opcode hex value of the 'AL' mnemonic is 00.
; That is the same opcode value as that of END.
; Thus, the program ends