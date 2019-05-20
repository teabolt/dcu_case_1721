# part 1 ("black" distribution - "D")

D_mean_x = 0
D_mean_y = 0
D_sd_x = 1.5
D_sd_y = 0.5
Dx = rnorm(1000, D_mean_x, D_sd_x)
Dy = rnorm(1000, D_mean_y, D_sd_y)

lim = c(-10, 10)
plot(Dx, Dy, xlim=lim, ylim=lim, xlab="x feature", ylab="y feature")


# part 2 ("blue" distribution - "B")

B_mean_x = -4
B_mean_y = 0
B_sd_x = 0.5
B_sd_y = 1.5
Bx = rnorm(1000, B_mean_x, B_sd_x)
By = rnorm(1000, B_mean_y, B_sd_y)

points(Bx, By, col="blue")


# part 3

my_mahalanobis = function(x, y, sdx, sdy) {
	return(x^2/sdx^2 + y^2/sdy^2)
}

from_black_to_black = my_mahalanobis(Dx, Dy, D_sd_x, D_sd_y)
from_black_to_blue = my_mahalanobis(Dx-B_mean_x, Dy, B_sd_x, B_sd_y) # have to account for the mean of the B distribution (it's x value is at -4, not 0)
from_blue_to_black = my_mahalanobis(Bx, By, D_sd_x, D_sd_y)
from_blue_to_blue = my_mahalanobis(Bx-B_mean_x, By, B_sd_x, B_sd_y)

B = cbind(Bx, By)
from_blue_to_blue2 = mahalanobis(B, c(B_mean_x, B_mean_y), cov(B))


# part 4

# # black misclassified as blue
points(Dx[from_black_to_blue < from_black_to_black], Dy[from_black_to_blue < from_black_to_black], col="red")

# # blue misclassified as black
points(Bx[from_blue_to_black < from_blue_to_blue], By[from_blue_to_black < from_blue_to_blue], col="orange")


# part 5

gx = seq(-10, 10, 0.1)
gy = gx

for (i in c(1:length(gx))) {
	for (j in c(1:length(gy))) {
		black = my_mahalanobis(gx[i], gy[j], D_sd_x, D_sd_y)
		blue = my_mahalanobis(gx[i]-B_mean_x, gy[j], B_sd_x, B_sd_y)
		
		if (black < blue) {
			# point is classified as black
			points(gx[i], gy[j])
		} else {
			# point is classified as blue
			points(gx[i], gy[j], col="blue")
		}
	}
}


# part 6

# the decision boundary is like a hourglass