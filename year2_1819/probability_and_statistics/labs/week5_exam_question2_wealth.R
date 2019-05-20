# Q2

wealth = c(80, 110, 110, 70, 120, 90, 110)
pop = c(.15, .20, .20, .10, .10, .10, .15)

sum(pop)

# (a)
m = sum(wealth*pop)
v = sum((m-wealth)^2*pop)

# (b)
twealth = wealth[4:7]
adjustment = 1/0.45
tpop = pop[4:7]*adjustment
tm = sum(twealth*tpop)
tv = sum((tm-twealth)^2*tpop)

# (c)
pt = sum(pop[4:7])
ptm100 = sum(pop[5], pop[7])
pm100_t = ptm100/pt

# (d)
pm100 = 0
for (i in c(1:7)) {
	if (100 < wealth[i]) {
		pm100 = pm100 + pop[i]
	}
}
pt_m100 = ptm100/pm100
