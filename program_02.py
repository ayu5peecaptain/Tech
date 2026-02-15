def var(x, mu, px):
    return sum((x - mu) **2 *px)

x = [2,3,5,7,9]
mu = sum(x) / len(x)
px = [0.1, 0.3, 0.25, 0.25, 0.1]

var(x, mu, px)