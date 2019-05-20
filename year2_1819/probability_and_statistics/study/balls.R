box = c(rep(1, 20), rep(0, 10))
N = 10000
picks = 0
takes = 0
for (i in c(1:N)) {
	pick = sample(box, 10, replace=T)
	take = sample(box, 10, replace=F)

	picks[i] = sum(pick)
	takes[i] = sum(take)
}
Dpicks = table(picks)/N
Dtakes = table(takes)/N

par(mfrow=c(2, 1))

plot(Dpicks, xlim=c(0, 10), xlab="Number of red balls with replacement", ylab="Probability")
Tpicks = dbinom(0:10, 10, 2/3)
points(c(0:10), Tpicks, col="red")

plot(Dtakes, xlim=c(0, 10), xlab="Number of red balls without replacement", ylab="Probability")
Ttakes = dhyper(0:10, 20, 10, 10)
points(c(0:10), Ttakes, col="green")
