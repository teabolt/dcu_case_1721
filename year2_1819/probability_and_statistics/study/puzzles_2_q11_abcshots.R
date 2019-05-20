shootOut = function(probs) {
	alive = rep(c(1), length(probs))
	bound = length(probs)
	i = 1
	j = 2
	repeat {
		hit = runif(1)
		if (hit < probs[i]) alive[j] = 0
		if (sum(alive) == 1) break

		i = incrementCyclic(i, bound)
		i = findCyclic(i, 1, alive, bound)

		j = i
		j = incrementCyclic(j, bound)
		j = findCyclic(j, 1, alive, bound)
	}
	return(min(which(alive == 1)))
}


incrementCyclic <- function(i, bound) {
	i = i + 1
	i = circle(i, bound)
	return(i)
}

circle <- function(i, bound) {
	if (bound < i) i = 1
	return(i)
}

findCyclic <- function(i, val, arr, bound) {
	while (arr[i] != val) {
		i = i + 1
		i = circle(i, bound)
	}
	return(i)
}

probs = c(0.5, 0.75, 0.5)
N = 1000000
winners = 0
for (i in c(1:N)) {
	winners[i] = shootOut(probs)
}
print(table(winners))
print(table(winners)/N)
plot(table(winners))
