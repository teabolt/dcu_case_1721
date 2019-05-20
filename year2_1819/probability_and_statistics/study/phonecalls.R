rate = 6 # phonecalls per minute
rate_second = rate/60 # phonecalls per second
N = 100000
phonecalls = 0
for (i in c(1:N)) {
	minute = sample(c(0, 1), 60, replace=T, prob=c(1-rate_second, rate_second))
	phonecalls[i] = sum(minute)
}

par(mfrow=c(2, 1))
plot(table(phonecalls)/N, xlim=c(0, 60), main="Phone call rates", xlab="Number of phonecalls in a minute", ylab="Probability")
points(dpois(0:60, rate), col="green")

waiting_time = 0
for (i in c(1:N)) {
	minute = sample(c(0, 1), 60, replace=T, prob=c(1-rate/60, rate/60))
	waiting_time[i] = min(which(minute == 1))
}
plot(table(waiting_time)/N, xlim=c(0, 60), main="Phone call waiting time", xlab="Seconds to wait until first phonecall", ylab="Probability")
# points(1-ppois(0:60, rate), col="yellow")
points(dexp(0:60, rate_second), col="yellow")