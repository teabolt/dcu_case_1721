N = 1000
e = exp(1:N)
p = c()
for (i in c(1:N)) p[i] = prod(1:i)

plot(e, log="y")
points(p, col="red")
# plot(exp(0), log="y")
# for (i in c(1:10)) {
# 	plot(exp(i), log="y")
# 	# points(prod(1:i), col="red")
# 	Sys.sleep(0.1)
# }