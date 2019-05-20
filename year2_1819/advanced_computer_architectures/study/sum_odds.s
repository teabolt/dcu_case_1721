    .text
    daddi r4, r0, 10    ; n = _
    daddi r3, r0, 1     ; odd = 1
    ;daddi r3, r0, 2     ; even = 2 (to sum evens)
    daddi r2, r0, 0     ; answer = 0

    loop:               ; while loop
        slt r1, r4, r3      ; set r1 to 1 if (n < odd) else to 0
        bnez r1, exit       ; if r1 is not zero (condition was true), finished
        dadd r2, r2, r3     ; answer  = answer + odd
        daddi r3, r3, 2     ; odd = odd + 2, eg: 1, 3, 5, 7, ...
        j loop

    exit:
        halt    ; answer in r2