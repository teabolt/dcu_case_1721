.data
    TRIANGLE: .word 3   ; TRIANGLE[0]
              .word 5   ; TRIANGLE[1]
              .word 2   ; TRIANGLE[2]
    LONGEST:  .word 0

.text
    daddi r1, r0, 8             ; i = 0
    daddi r2, r0, 24            ; N = 3*8 = 24
    ld r3, TRIANGLE(r0)      ; guess = TRIANGLE[0]
    loop:
        ld r4, TRIANGLE(r1)     ; curr = TRIANGLE[i]
        beq r1, r2, finish
        ; bds
        slt r5, r3, r4          ; set r5 = 1 if guess < curr, else 0
        nop
        beqz r5, loop           ; if curr >= guess, skip
        ; bds
        daddi r1, r1, 8         ; i = i + 1
        j loop                  ; check next
        ; bds
        daddi r3, r4, 0         ; guess = curr
    
    finish:
        sd r3, LONGEST(r0)
        halt