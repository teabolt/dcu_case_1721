.data
    arrint: .word 5
            .word -3
            .word 4
            .space 776
    .word 2

.text
    daddi r1, r0, 0     ; i = 0
    daddi r2, r0, 800   ; N = 100
    daddi r3, r0, 3     ; m = 3
    loop:
        beq r1, r2, finish

        ld r11, arrint(r1)      ; <- [i]
        ld r12, arrint+8(r1)    ; <- [i+1]
        dmul r11, r11, r3
        dmul r12, r12, r3
        ld r13, arrint+16(r1)   ; <- [i+2]
        ld r14, arrint+24(r1)   ; <- [i+3]
        dmul r13, r13, r3
        dmul r14, r14, r3

        ld r15, arrint+32(r1)   ; <- [i+4]

        dmul r15, r15, r3

        sd r11, arrint(r1)      ; -> [i]
        sd r12, arrint+8(r1)    ; -> [i+1]
        sd r13, arrint+16(r1)   ; -> [i+2]
        sd r14, arrint+24(r1)   ; -> [i+3]
        sd r15, arrint+32(r1)   ; -> [i+4]

        j loop
        daddi r1, r1, 40        ; i += 5
        

    finish:
        halt