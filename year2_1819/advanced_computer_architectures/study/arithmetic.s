.data
    a: .double 1
    b: .double 2

.text
    daddi r1, r0, 12124241421
    daddi r2, r0, 2
    ddiv r3, r1, r2

    l.d f0, a(r0)
    l.d f1, b(r0)
    div.d f2, f0, f1

    ori r4, r3, -1

    halt