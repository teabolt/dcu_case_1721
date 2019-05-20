.text

; Program to add four numbers together
; Make sure that all menu options on WinMips64 Simulator are
; switched off
              daddi r1,r0,11         ; r1=11;
              daddi r2,r0,22         ; r2=22;
              daddi r3,r0,33         ; r3=33;
              nop
              dadd r5,r1,r2          ; r5=r1 + r2;
              nop
              daddi r4,r0,44         ; r4=44;  
              dadd r5,r5,r3          ; r5 += r3;
              nop
              nop
              dadd r5,r5,r4          ; r5 += r4;

              halt