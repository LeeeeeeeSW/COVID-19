def Disease():
        print("\n Desease")
        print("\n\tInfectRate : ")
        #정규분포
        global infectRate
        infectRate = float(input())
        print("\n\tDeathRate : ")
        #정규분포
        global deathRate
        deathRate = float(input())
        global death
        death = 0

def Background():
	print("population : ")
	global population
	population = int(input())
	print("contact average : ")
        #정규분포
	global contactavr
	contactavr = int(input())
        

Disease()
Background()
student = {}
for i in range(1,population+1):
        student[i] = "normal"

print(student)
