v_p = 0
v_n = 0
g_p = 0
g_n = 0
count = 0
true_pos = 0
N = 100000
for (i in c(1:N)) {

	if (runif(1) < 0.15) {
		if (runif(1) < 0.95) {
			v_p = v_p + 1
			count = count + 1		
			true_pos = true_pos + 1
		} else {
			v_n = v_n + 1
		}
	} else {
		if (runif(1) < 0.02) {
			g_p = g_p + 1
			count = count + 1		
		} else {
			g_n = g_n + 1
		}
	}
}
print(v_p/N)
print(v_n/N)
print(g_p/N)
print(g_n/N)
p = v_p + g_p
print(p/N)
print((v_p/N)/(p/N))	# P(v|p)
print(true_pos/count)
