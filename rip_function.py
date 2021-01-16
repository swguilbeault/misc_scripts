lines = open("split/Sorted_List.c", "r").read().split("\n")

for line in lines:
    if len(line) > 0:
        if (line[0] != " " and line[0] != "\t" and line[-1] == "{"):
            print(line[0:-2] + ";")
        elif (line[0:3] in ["#if", "#en"]):
            print(line)