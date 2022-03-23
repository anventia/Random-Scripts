d = 3
count = 1000000
output = 1
for i in range(count):
	if i % 2 == 0:
		output -= (1/d)
	else:
		output += (1/d)
	d += 2

print(output*4)