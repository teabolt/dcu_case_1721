; Control the traffic lights

; Send a byte: in binary representation 0000_0000, 
; if a bit is 1, the light lights up
; if a bit is 0, the light stays unlit
; which light lights up depends on the position of the 'one' bits
; the last two least significat bits are unused
; going up from the LSB to the MSB, first the green lights up, then the yellow, then the red
; first the right traffic light activates, then the left one

CLO			; close unwanted windows
; set the right light to green
MOV AL, 04		; data to send
OUT 1			; port for traffic lights
; set the right light to red
MOV AL, 10
OUT 1
END			; unique exit