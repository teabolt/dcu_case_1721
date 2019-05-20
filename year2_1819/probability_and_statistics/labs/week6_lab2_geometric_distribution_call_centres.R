p = 0.1

waits = 0
N = 10000
for (i in c(1:N)) {
	minute = sample(c(0, 1), 60, replace = T, prob=c(1-p, p))
	j = 1
	while(j <= 60 & minute[j] != 1) j = j + 1
	if (j <= 60)
		waits[i] = j - 1
	else
		waits[i] = -1
	# print(minute)
	# print(waits[i])
}

table(waits)
plot(table(waits), type='h')

q = 1 - p
points(c(1:60), N*q^(0:59)*p)