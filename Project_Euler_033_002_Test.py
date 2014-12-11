Product_N = 1
Product_K = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        str_i = str(i)
        str_j = str(j)
        Flag = False
        for k in range(2):
            for l in range(2):
                if str_i[k] == str_j[l] and str_i[k] != '0':
                    str_i = str_i[:k] + str_i[k + 1:]
                    str_j = str_j[:l] + str_j[l + 1:]
                    Flag = True
                    break
            if Flag == True:
                break
        else:
            continue
        if float(str_j) == 0:
            continue
        if float(i) / j == float(str_i) / float(str_j):
            Product_N *= i
            Product_K *= j
print Product_N, Product_K
print Product_K / Product_N
Wait = raw_input()