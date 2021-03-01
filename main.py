files = ["a", "b", "c", "d", "e", "f"]

inputFilename = files[0] + ".txt"
outputFilename = inputFilename + ".out"

with open(inputFilename, "r") as f:
	input = f.readlines()

print(input)


duration = int(input[0].split(" ")[0])
intersectionnum = int(input[0].split(" ")[1])
streetnum = int(input[0].split(" ")[2])
carnum = int(input[0].split(" ")[3])
bonus = int(input[0].split(" ")[4])

input.pop(0)



streets = []
for i in range(streetnum):
	streets += [input[0].replace("\n", "").split(" ")]
	input.pop(0)

cars = []
for car in input:
	cars += [car.replace("\n", "").split(" ")]

for i in range(len(streets)):
	streets[i] = [int(streets[i][0])] + [int(streets[i][1])] + [streets[i][2]] + [int(streets[i][3])]

for i in range(len(cars)):
	cars[i][0] = int(cars[i][0])


print("Duration: {0} Intersections: {1} Streets: {2} Cars: {3} Bonus: {4}".format(duration, intersectionnum, streetnum, carnum, bonus))
print(streets)
print(cars)

popularity = {}

for street in streets:
	popularity[street[2]] = 0

	for car in cars:
		if street[2] in car:
			popularity[street[2]] += 1


intersections = {}
for i in range(intersectionnum):
	intersections[i] = []
	for street in streets:
		if street[1] == i:
			intersections[i] += [street[2]]

print(intersections)

for i in range(intersectionnum):
	for q in range(len(intersections[i])):
		for j in range(len(intersections[i])-1):
			if popularity[intersections[i][j]] < popularity[intersections[i][j + 1]]:
				temp=intersections[i][j]
				intersections[i][j]=intersections[i][j+1]
				intersections[i][j+1]=temp


output = ""
output += "{}\n".format(intersectionnum)
for i in range(intersectionnum):
	output += "{}\n".format(i)
	output += "{}\n".format(len(intersections[i]))
	for j in range(len(intersections[i])):
		if j == 0:
			time = (popularity[intersections[i][j]] // 2) + 3
		else:
			time = (popularity[intersections[i][j]] // 2) + 1

		output += "{0} {1}\n".format(intersections[i][j], time)

output = output[:-1]

with open(outputFilename, "w") as f:
	f.write(output)
