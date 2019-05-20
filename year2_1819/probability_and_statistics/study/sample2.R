Xh = c()
Xb = c()
size = 100000
for(i in c(1:size))
{
	h = sample(c(rep(0, 15), rep(1, 5)), 5, replace = F)
	b = sample(c(rep(0, 15), rep(1, 5)), 5, replace = T)
	
	Xh[i] = sum(h)
	Xb[i] = sum(b)
}
table(Xh)
table(Xb)

par(mfrow = c(2,1))
plot(table(Xh))
points(c(0:5),dhyper(0:5, 5, 15, 5)*size, col="red") 
plot(table(Xb))
points(c(0:5),dbinom(0:5, 5, 0.25)*size, col="blue")
