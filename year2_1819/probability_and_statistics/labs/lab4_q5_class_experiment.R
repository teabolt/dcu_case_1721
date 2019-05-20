all_f = 0
N = 10000
for(i in c(1:N)) {
	s = sample(c(rep('f', 60), rep('m', 40)), 5, replace=F)
	if (s == 'f') {
		all_f = all_f + 1
	}
}
print(all_f)