Xr = 0
Xn = 0
size = 1000
for(i in c(1:size))
{
	r = sample(c(rep(1,20),rep(0,10)), 10, replace=T)
	n = sample(c(rep(1,20),rep(0,10)), 10, replace=F)

	Xr[i] = sum(r)
	Xn[i] = sum(n)

}
table(Xr)
table(Xn)
plot(table(Xr))
points(table(Xn), col='red')