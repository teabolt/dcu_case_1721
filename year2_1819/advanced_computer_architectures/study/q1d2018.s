.data
    LENGTH: .word 0
    MyArray: .word 11 ; Array[0]
    .word 22 ; Array[1]
    .word 33 ; Array[2]

.text
    daddi r1,r0,0
    ld r5, MyArray(r1)
    dadd r1,r0,r5
    halt