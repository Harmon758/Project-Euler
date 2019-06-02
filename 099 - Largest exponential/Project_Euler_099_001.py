from math import log10

Base_Exp_File = open("p099_base_exp.txt", 'r')
Base_Exps = []
for Line in Base_Exp_File.readlines():
	Base_Exps.append(map(int, Line.split(',')))
Largest = 0
Largest_Index = 0
for Base_Exp in Base_Exps:
	if Base_Exp[1] * log10(Base_Exp[0]) > Largest:
		Largest = Base_Exp[1] * log10(Base_Exp[0])
		Largest_Index = Base_Exps.index(Base_Exp)
print Largest_Index + 1
Wait = raw_input()