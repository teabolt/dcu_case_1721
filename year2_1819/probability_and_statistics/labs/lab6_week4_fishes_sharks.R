N = 1000
fishes[1] = 20
sharks[1] = 5
for (month in c(2:N)) {
	nfishes = fishes[month-1]
	nsharks = sharks[month-1]

	# fish growth
	fishes[month] = fishes[month-1]
	for (fish in c(1:fishes[month-1])) {
		if (runif(1) < 0.01) {
			nfishes = nfishes + 1
		}
	}
	
	# shark death
	for (shark in c(1:sharks[month-1])) {
		if (runif(1) < 0.01) {
			nsharks = nsharks - 1
		}
	}

	# how many meet each other
	for (fish in c(1:fishes[month-1])) {
		if (runif(1) < sharks[month-1]/1000) {
			nfishes = nfishes - 1
			nsharks = nsharks + 1
		}
	}

	if (nfishes < 5) {
		nfishes = 5
	}
	if (nsharks < 5) {
		nsharks = 5
	}

	fishes[month] = nfishes
	sharks[month] = nsharks
	
}
plot(sharks)
points(fishes, col='red')