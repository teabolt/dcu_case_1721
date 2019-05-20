count = 0
N = 10000
for(i in c(1:N)) {
	s = sample(c(rep("r", 15), rep("g", 10), rep("b", 5)), 5, replace=F)
	# print(s)
	if(s[1] == "r" & s[2] == "r" & s[3] == "r" & s[4] == "r" & s[5] == "r") {
		count = count + 1
	}
}
count
count/N