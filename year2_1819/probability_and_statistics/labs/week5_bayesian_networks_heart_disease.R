s = 0.3
d = 0.4

h_sd = 0.8
h_0sd = 0.5
h_s0d = 0.4
h_0s0d = 0.1

b_h = 0.7
b_0h = 0.1
e_h = 0.8
e_0h = 0.1

# (i)
h = h_sd*s*d + h_0sd*(1-s)*d + h_s0d*s*(1-d) + h_0s0d*(1-s)*(1-d)

# (ii)
b = b_h*h + b_0h*(1-h)

# (iii)
h_b = (b_h*h)/b

# (iv)
be = b_h*e_h*h + b_0h*e_0h*(1-h)

# (v)
h_be = (b_h*e_h*h)/be

# (vi)
b0e = b_h*(1-e_h)*h + b_0h*(1-e_0h)*(1-h)
h_b0e = (b_h*(1-e_h)*h)/b0e

# (vii)
h_s = h_sd*d + h_s0d*(1-d)

# (viii)
e_s = h_s*e_h + (1-h_s)*e_0h

# (ix)
es = e_s*s
s_h = (h_s*s)/h
es_h = e_h*s_h
h_es = (es_h*h)/es