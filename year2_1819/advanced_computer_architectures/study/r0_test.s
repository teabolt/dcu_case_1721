.text
    daddi r0, r0, 10    ; check if r0 can be set to something non-zero
    daddi r1, r0, 0     ; move r0 into r1
    halt ; result - setting r0 to something else does not work. It gets ignored