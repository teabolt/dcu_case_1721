JMP start	; Jump IP to address 16 (start label)
DB 09
DB 20
DB 21
DB 22
DB 23
ORG 16		; Start at address 16(hex)
start:								; Original addresses
	CLO 		; Close unwanted windows.		; Program starts at address 00
	MOV AL, 00 	; Copy a 0 into the AL register.	; At address 01 to 03 inclusive
	ADD AL, 01 	; Add 01 to AL. Answer goes into AL.	; At address 04 to 06 inclusive
	END 		; Program ends				; At address 7