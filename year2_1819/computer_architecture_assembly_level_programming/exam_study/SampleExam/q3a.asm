; Six-digit Exam number:  17350793
; Seat Number (if available)	17

; Character converter
; Reads (using the simple keyboard) a lowercase character (a-z letter) 
; and converts it to an uppercase character (corresponding A-Z letter), 
; displayed on the top left of the VDU.

; Relevant ASCII:
; 'a' to 'z': 61 to 7A
; 'A' to 'Z': 41 to 5A
; difference factor: +-20



main:		; entrance point to program	
	CLO 		; close unused windows
	IN 00		; read a character from the simple keyboard (result in AL)
	CALL 20		; verify the character (BL=FF if not lowercase)
	CMP BL, FF	; exit if not lowercase
	JZ end		
	CALL 40 	; uppercase the character
	MOV CL, C0	; point to top left of the VDU	
	CALL 60		; display the character
	end:
		HALT	; stop the CPU



ORG 20		; procedure VERIFY_LOWER, verifies that a character is a lowercase letter (in ASCII)
; Input: AL (the character)
; Output: BL = FF if NOT lowercase, else no output
; Destroys: BL
	; check lower bound (60)
	MOV BL, 60
	CMP BL, AL	; S set if BL < AL
	JNS false_vl
	; check upper bound (7B)
	MOV BL, 7B
	CMP AL, BL	; S set if AL < BL
	JNS false_vl
	RET		; in bounds
	
	false_vl: ; the character is not lowercase
		MOV BL, FF
		RET
	; TODO: parameterise the procedure so that it checks that a character is between two bounds that are passed as parameters		
	

ORG 40		; procedure TO_UPPER, converts a lowercase ASCII letter to its uppercase version
; Input: AL (the letter)
; Output: AL (in uppercase form)
	SUB AL, 20	; use "constant difference" in the ASCII table to convert to uppercase
	RET
	; TODO: 'transform' procedure that includes more character transforms, eg: to lower, etc



ORG 60		; procedure DISPLAY, displays a character on a cell of the VDU
; Input: AL (the character), CL (the VDU location)
	MOV [CL], AL	; write the character to the VDU
	RET
	; TODO: more advanced display parameters - repeat the character, etc

		

END		; end of source code