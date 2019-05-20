calls = 0
waits = 0
N = 10000
for (i in c(1:N)) {
	minute = sample(c(0, 1), 60, replace=T, prob=c(0.9, 0.1))
	calls[i] = sum(minute)
	waits[i] = min(which(minute == 1))
}

par(mfrow=c(1, 2))
call_distr = table(calls)
plot(call_distr, "h")
points(c(0:60), dpois(c(0:60), 6)*N, col="blue")

wait_distr = table(waits)
plot(wait_distr)
points(c(0:60), pexp(6/60), col="red")