.text   ; a program that puts a maximum integer value (unsigned) to a register (all 1's)
    dadd r1, r0, r0     ; result register
    daddi r2, r0, 1     ; register with 1 in it
    dsubu r3, r1, r2     ; 0 - 1 = -1 (overflow/flip)
    halt