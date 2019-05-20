arrive_p = 2/60
serve_p = 1/60

queue1 = 0
queue2 = 0
N = 1000
for (i in c(2:N)) {
	arrivals = sum(sample(c(0, 1), 60, replace=T, prob=c(1-arrive_p, arrive_p)))
	departures1 = sum(sample(c(0, 1), 60, replace=T, prob=c(1-serve_p, serve_p)))
	departures2 = sum(sample(c(0, 1), 60, replace=T, prob=c(1-serve_p, serve_p)))

	# number_arrived = sum(arrivals == 1)
	# number_served = sum(departures == 1)
	if (queue1[i-1] <= queue2[i-1]) {
		queue1[i] = max(queue1[i-1] + arrivals - departures1, 0)
		queue2[i] = max(queue2[i-1] - departures2, 0)
	} else {
		queue2[i] = max(queue2[i-1] + arrivals - departures2, 0)
		queue1[i] = max(queue1[i-1] - departures1, 0)
	}
}

# par(mfrow=c(1, 1))
plot(queue1)
# plot(queue2)
points(queue2, col='red')