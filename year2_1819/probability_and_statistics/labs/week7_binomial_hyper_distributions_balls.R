p = 1/4
q = 1-p
box = c(rep(0, 15), rep(1, 5))

replace_blacks = 0
noreplace_blacks = 0
N = 10000
for (i in c(1:N)) {
	replace_balls = sample(box, 5, replace=T)
	noreplace_balls = sample(box, 5, replace=F)
	replace_blacks[i] = sum(replace_balls)
	noreplace_blacks[i] = sum(noreplace_balls)
}
print(table(replace_blacks))
print(table(noreplace_blacks))

par(mfcol=c(1, 3))

# plot with replacement
plot(table(replace_blacks), title="with replacement", xlab="X", ylab="sample number")
bin = dbinom(0:5, 5, p)*N
points(c(0:5), bin)

# plot without replacement
plot(table(noreplace_blacks), title="without replacement", xlab="X", ylab="sample number")
hyp = dhyper(c(0:5), 5, 15, 5, p)*N
points(c(0:5), hyp)