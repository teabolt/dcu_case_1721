.data

CONTROL: .word 0x10000     ; associate label CONTROL with some memory location, storing in it an 8-byte hex value
DATA:    .word 0x10008     ; these are IO ports
str: .asciiz "dlroW olleH" ; zero terminated ASCII characters

.text
main:
   ; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
   ; load memory-mapped IO addresses
   ld r20,CONTROL(r0)      ; use high registers
   ld r21,DATA(r0)
   daddi r1,r0,0 ; i, initalise pointer variable (points to a position in str)
   ; first, find the end of the string (the string is null terminated, so
   ; that's the first zero byte).
loop1:   ; find index of last character
   lb r3,str(r1)  ; load the character currently pointed at (starting at str, offset/displace by r1)
   beqz r3,done1 ; we're done if the byte we read is zero (branch equal zero - branch taken to done1 if r3 is zero)
   nop;XXX
   daddi r1,r1,1 ; i += 1 (increment pointer)
   j loop1       ; jump
   nop;XXX
done1:
   ; r1 (i) now points to the byte *after* the last character in the string (points to the zero sentinel)
   ; r1 (i) now traverses the string from right to left (<-) (right/hi ptr)
   ; r2 (j) now traverses the string from left to right (->) (left/lo ptr)
   ; we stop when r1 < r2 (i < j)  - when the pointers cross
   daddi r1,r1,-1 ; i -= 1 ; get to the actual last character (or dsubi? - immediate only for add?)
   daddi r2,r0,0  ; j = 0
loop2:   ; reverse the string (go half way through)
   slt r5,r1,r2   ; set r5 if r1 < r2 (i < j) - set r5 to 1 if true, else to 0, lt = r1 less than r2
   bnez r5, done2 ; stop if r1 < r2 - if r5 != 0, stop (0 - continue, 1 - stop!)
   nop;XXX
   ; swap str[i] (str[r1]) and str[j] (str[r2])
   lb r3,str(r1) ; r3 = str[i], get the characters (load byte = load 1 byte - ASCII character)
   lb r4,str(r2) ; r4 = str[j]
   sb r4,str(r1) ; into str[i] store what's in r4 (store byte = store 1 byte) (store left in right)
   sb r3,str(r2) ; into str[j] store what's in r3
   daddi r1,r1,-1 ; i -= 1 - move r1 (i) backwards
   daddi r2,r2,1  ; j += 1 - move r2 (j) forewards
   j loop2
   nop;XXX
done2:
   ; the string has now been reversed in memory
   ; output it to the terminal
   daddi r1,r0,str  ; place start address of str in r1
   sd r1,0(r21)     ; set DATA to output value (address of string, here) (move starting address of str to starting address of DATA in memory) (only need the starting address for strings! - zero/null terminated - knows when to stop)
   daddi r1,r0,4    ; init control signal (4 - string output, 3 - float, 2 - signed int)
   sd r1,0(r20)     ; write CONTROL (place the actual control signal - something happens)
   halt