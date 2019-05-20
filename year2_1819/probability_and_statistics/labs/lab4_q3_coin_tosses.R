v = 0 # result vector
for(i in c(1:10000)) {
	v[i] = sample(c("H", "T"), 1, replace=T)
}
table(v)