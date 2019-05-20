; Mutiple each array element by three and add 5
.data
Triple:   .word 10 ; Triple[0] = 10
          .word 20 ; Triple[1] = 20
          .word 30 ; Triple[2] = 30
.text

; Insert your modified code
; with the loop unrolled
;
  daddi r1, r0, 0    ;index into array
  daddi r3, r0, 24   ;check when to stop (3 element x 8 bytes = 24)
  daddi r2, r0, 3   ; Multiplier by Three

do_again:
  ; unroll three iterations of the loop
  ; use different registers
  ; do multiplication first since it takes longest

  ld r5, Triple(r1)     ;load first element in
  beq r1, r3, end       ; XXX
  dmul r4,r2,r5     ;r4 = 3x(Triple[i]) ; use the BDS (ignore if branch is taken)
  ld r7, Triple+8(r1)
  ld r9, Triple+16(r1)
  dmul r6,r2,r7     ;r4 = 3x(Triple[i])
  dmul r8,r2,r9     ;r4 = 3x(Triple[i])

; some stalls will still exist when adding r4 and r6
  daddi r4,r4,5     ;r4 = 3x(Triple[i]) + 5
  sd r4, Triple(r1)

  daddi r6,r6,5     ;r4 = 3x(Triple[i]) + 5
  sd r6, Triple+8(r1)

  daddi r8,r8,5     ;r4 = 3x(Triple[i]) + 5
  sd r8, Triple+16(r1)

  j do_again             ; XXX
  daddi r1, r1, 24        ; next starting index ; use BDS

end:
  halt