.data

LENGTH: .word 0     ; init length of triangle

Triangle: .word 11 ; Triangle[0] ; side 1

          .word 22 ; Triangle[1] ; side 2

          .word 33 ; Triangle[2] ; side 3


.text


 daddi r1, r0, 0    ;index into array

 daddi r3, r0, 24   ;check when to stop (8+8+8 = 24 (3 doublewords))

 daddi r4, r0, 0   ; Length = 0; ; init curr length



repeat:

 ld r5, Triangle(r1)    ;load first element in



 beq r1, r3, end ; XXX

 dadd r4,r4,r5    ;sum = sum + Triangle[i]

 daddi r1, r1,8        ; next index (+8, a doubleword forward)

 j repeat             ; XXX


end:

 sd r4, LENGTH(r0)  ; store doubleword in LENGTH, from r4

halt