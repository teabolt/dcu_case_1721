.data
    D: .double -3.0, 2.3 ; values at Mem[0] and Mem[8]
    .space 64
    I: .word32 421
    pos: .word16 18
    neg: .word16 -20
    res: .space 4
    res2: .space 8

.text
    ; loads and stores
    ;daddi r1, r0, 1234
    ;daddi r2, r0, 9999
    ;l.d f1, D(r0) ; Mem[0]
    ;daddi r10, r0, 8 ; 8 bytes offset
    ;l.d f2, D(r10) ; Mem[8]
    ;sd r1, 16(r0) ; Mem[16]
    ;add.d f3, f1, f2
    ;s.d f3, 24(r0) ; Mem[24]

    ; signed stuff
    ;lhu r4, pos(r0)
    ;lhu r5, neg(r0)
    ;daddu r6, r4, r5
    ;sh r6, res(r0)

    ; unmatched store bits
    daddi r7, r0, -1
    sw r7, res2(r0)

    ; half loads
    ; lui r8, 10
    ; ???


    
    halt

; question - are .text and .data separate "logical address spaces"?