def test(x, y):
	tmp = x
	x = y
	y = tmp
	return y.append(x)

x = ["y"]
y = ["x"]

print(test(x, y))