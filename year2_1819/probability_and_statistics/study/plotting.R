x = c()
y = c()
for (i in c(1:100)) {
	x[i] = i^2+i+5
	y[i] = 2*i^2+i-5
	plot(x)
	points(y, col='red')
	Sys.sleep(0.1)
}


plot(c(-10:10), c(-10:10))