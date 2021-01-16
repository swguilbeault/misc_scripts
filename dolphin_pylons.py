print("######### Dolphin Pylon Location Calculator #########\n#")

#pos1 = [int(i) for i in input("# Location 1 (X Y Z): ").strip().split(" ")]
#pos2 = [int(i) for i in input("# Location 1 (X Y Z): ").strip().split(" ")]

pos1 = [769, 57, -440]
pos2 = [1656, 57, -96]

vector = [(pos2[i] - pos1[i]) for i in range(3)]
distance = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5

print("# Distance :" + str(distance))
print("# dx/dz : "+ str(vector[0] / vector[2]))

n = int(distance / 60)
vector_p = [vector[i] / (n + 1.0) for i in range(3)]

print("#\n# WITHOUT DEPTH STRIDER: \n# \t" + str(pos1) + " <<< start")
for i in range(n):
    print("# \t" + str([(round(pos1[j] + vector_p[j] * (i+1))) for j in range(3)]) + (" <<<" if i % 3 == 2 else ""))
print("# \t" + str(pos2) + " <<< end")

    
    
n = int(distance / 180)
vector_p = [vector[i] / (n + 1.0) for i in range(3)]

print("# \n# WITH DEPTH STRIDER: \n# \t" + str(pos1) + " <<< start")
for i in range(n):
    print("# \t" + str([(round(pos1[j] + vector_p[j] * (i+1))) for j in range(3)]))
print("# \t" + str(pos2) + " <<< end")

print("# \n####################### swg ########################")

