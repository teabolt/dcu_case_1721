.data
    TRIANGLE: .word 5   ; TRIANGLE[0]
              .word 2   ; TRIANGLE[1]
              .word 3   ; TRIANGLE[2]
    LENGTH:   .word 0

.text
    daddi r2, r0, 24    ; N = 3*8 = 24
    daddi r1, r0, 8     ; i = 1
    ld r9, TRIANGLE(r0) ; sum = TRIANGLE[0] (initialise)
    loop:
        beq r1, r2, finish  ; i == N ?
        ; bds
        ld r5, TRIANGLE(r1) ; curr = TRIANGLE[i]
        daddi r1, r1, 8     ; i = i + 1
        j loop
        ; bds
        dadd r9, r9, r5     ; sum = sum + curr

    finish:
        sd r9, LENGTH(r0)
        halt