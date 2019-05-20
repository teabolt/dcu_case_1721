; Get the minimum and the maximum of an array

.data
    MIN: .space 8 ; minimum value
    MAX: .space 8 ; maximum value
    arrint:       ; arrint[100]
        .word 51  ; arrint[0]
        .word 15  ; arrint[1]
        .word 64  ; arrint[2]
        .word 5   ; arrint[3]
        .word -4  ; arrint[4]
        .word 13  ; arrint[5]
        .space 760 ; 100*8 - 5*8 = 760 (the rest of the integers)

.text
    daddi r1, r0, 8     ; i = 1
    daddi r2, r0, 800   ; N = 100
    ld r10, arrint(r0)  ; min_guess = arrint[0], assume non-empty arrint
    ld r11, arrint(r0)  ; max_guess = arrint[0]
    loop:
        ld r3, arrint(r1)   ; curr = arrint[i]
        ; update min_guess
        slt r4, r3, r10     ; curr < min_guess ?
        beqz r4, check_max  ; if false, try update max_guess
        daddi r1, r1, 8     ; (BDS), i += 1
        ; not false, update min
        daddi r10, r3, 0    ; min = curr
        j next
        nop                 ; (BDS)
        check_max:
            slt r4, r11, r3     ; max < curr ?
            beqz r4, next       ; if false, go to next
            nop                 ; (BDS)
            ; not false, update max
            daddi r11, r3, 0    ; max = curr
        next:
            slt r4, r1, r2 ; (i < N) ?
            bnez r4, loop  ; if true, do next iteration
            nop            ; (BDS)
    ; finished
    sd r10, MIN(r0)
    sd r11, MAX(r0)
    halt