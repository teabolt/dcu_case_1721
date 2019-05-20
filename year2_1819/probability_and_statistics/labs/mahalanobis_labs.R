#rnorm  arguments = (sample size, mean_x/y_value, std_dev_x/y )

x = rnorm(1000, 0.0, 1.5)
y = rnorm(1000, 0.0, 0.5)

rng = c(-10, 10)
plot(x, y, xlim = rng, ylim = rng)

############################################################

a = rnorm(1000, -4.0, 0.5)
b = rnorm(1000, 0.0, 1.5)

points(a, b, col="blue")

############################################################
M_black_black = x^2/(1.5^2) + y^2/(0.5^2)
M_blue_black  = a^2/(1.5^2) + b^2/(0.5^2)

M_black_blue = (x+4)^2/(0.5^2) + y^2/(1.5^2)
M_blue_blue  = a^2/(0.5^2) + b^2/(1.5^2)

points(x[M_black_black > M_black_blue], y[M_black_black > M_black_blue], col="red")
points(x[M_blue_black > M_blue_blue], y[M_blue_black > M_blue_blue], col="orange")

############################################################
gx = seq(-10, 10, 0.1)
gy = gx

M1 = gx^2/(1.5^2)+gy^2/(0.5^2) # black class
M2 = gx^2/(0.5^2)+gy^2/(1.5^2) # blue class
points(gx[M1 < M2], gy[M1 < M2]) # closer to black
points(gx[M2 < M1], gy[M2 < M1], col="blue") # closer to blue