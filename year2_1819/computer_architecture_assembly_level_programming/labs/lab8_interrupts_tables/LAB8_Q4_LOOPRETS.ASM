; Have a procedure switch alternate its returning addresses between two loops

loop1:	; address 0
  INC BL
  CALL 50
  JMP loop1 ;---- line 4 - at address 04

ORG 10
loop2:	; address 10
  INC CL
  CALL 50
  JMP loop2 ;---- line 9 - at address 14

ORG 50
  ;The code in here should do a weird trick. See above....
  POP AL	; move the saved IP value (what to return to) to a general purpose register
  CMP AL, 4	; IP is for loop 1
  ; change to return to the 'head' of each loop: (KEEP THE CMP SAME! - WHERE CALLING FROM)
  JZ mk_loop2

  ; mk_loop1
  ;MOV AL, 4		; line of loop 1
  MOV AL, 0
  JMP proc_end

  mk_loop2:
  ;MOV AL, 14	; line of loop 2
  MOV AL, 10

  proc_end:
	PUSH AL ; save back the value as the new IP address
  	RET


END