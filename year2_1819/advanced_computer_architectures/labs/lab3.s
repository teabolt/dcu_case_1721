.data

CONTROL: .word 0x10000
DATA:    .word 0x10008
str: .ascii "dlroW olleH"
.text
main:
   ; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
   ; load memory-mapped IO addresses
   ld r20,CONTROL(r0)
   ld r21,DATA(r0)
   daddi r1,r0,0 ; i
   ; first, find the end of the string (the string is null terminated, so
   ; that's the first zero byte).
loop1:
   lb r3,str(r1)
   beqz r3,done1 ; we're done if the byte we read is zero
   nop;XXX
   daddi r1,r1,1 ; i += 1
   j loop1
   nop;XXX
done1:
   ; r1 (i) now points to the byte *after* the last character in the string
   ; r1 (i) now traverses the string from right to left
   ; r2 (j) now traverses the string from left to right
   ; we stop when r1 < r2 (i < j)
   daddi r1,r1,-1 ; i -= 1
   daddi r2,r0,0  ; j = 0
loop2:
   slt r5,r1,r2   ; set r5 if r1 < r2 (i < j)
   bnez r5, done2 ; stop if r1 < r2
   nop;XXX
   ; swap str[i] (str[r1]) and str[j] (str[r2])
   lb r3,str(r1)
   lb r4,str(r2)
   sb r4,str(r1)
   sb r3,str(r2)
   daddi r1,r1,-1 ; i -= 1 ; move r1 (i) backwards
   daddi r2,r2,1  ; j += 1 ; move r2 (j) forewards
   j loop2
   nop;XXX
done2:
   ; the string has now been reversed in memory
   ; output it to the terminal
   daddi r1,r0,str
   sd r1,0(r21)     ; set DATA to output value (address of string, here)
   daddi r1,r0,4
   sd r1,0(r20)     ; write CONTROL
   halt