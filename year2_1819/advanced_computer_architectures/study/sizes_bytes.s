.text       ; code area
    daddi r1, r0, 8     ; double word immediate add, store in r1 (pattern to load numbers into registers)
    ; check double word
    daddi r2, r0, 64    ; double word immediate add, store in r2, add 0 (r0) to 64 (base 10)
    ddivu r2, r2, r1    ; unsigned division
    ; check word
    daddi r3, r0, 32
    ddivu r3, r3, r1
    ; check half-word
    daddi r4, r0, 16
    ddivu r4, r4, r1
    ; check byte
    daddi r5, r0, 8
    ddivu r5, r5, r1
    halt                ; stop the program (else it keeps going)