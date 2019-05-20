.text   ; example to show the overflow of signed arithmetic in comparison to unsigned arithmetic
    dadd r1, r0, r0     ; initialise to zero
    daddi r2, r0, 1
    dsub r1, r1, r2     ; get r1 to be all 1's
    ;dsrl r1, r1, 4      ; shift by 1 to get a leading 0 and all 1's after it (half way in signed numbers)
    daddi r3, r0, 2    
    ;ddiv r1, r1, r3    ; alternative to shifting
    ddiv r4, r1, r3     ; divide -1 by 2 signed -> zero
    ddivu r5, r1, r3    ; divide max number by 2 unsigned -> half

    daddi r10, r0, 64
    daddi r11, r0, 4
    ddiv r10, r10, r11
    halt