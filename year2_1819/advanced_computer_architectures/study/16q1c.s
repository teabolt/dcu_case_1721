.data
    VALUE: .word 10
    OUTPUT: .space 8

.text
    ;ld r1, VALUE(r0)
    ;sd r2, OUTPUT(r1)
    
    daddi r1, r0, 32
    ;jr r1
    daddi r2, r1, 10
    halt