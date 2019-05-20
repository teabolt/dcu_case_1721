join <- function(shots, skill) {
	sum(dbinom(0:shots, shots, skill)[(shots/2+1):(shots+1)])
}

distr <- function(shots, step) {
	probs = 0
	vect = seq(0, 1, step)
	for (i in 1:length(vect)) {
		probs[i] = join(shots, vect[i])
		print(paste(vect[i], probs[i]))
	}
	probs
}

step = 0.01
plot(seq(0, 1, step), distr(6, step))
points(seq(0, 1, step), distr(4, step), col="red") 
print(0.6)