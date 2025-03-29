list_number = [1,2,3,4,5,6]
for i ,j in enumerate(list_number):
    print(i,j)
    print("---------------------")
    if i % 2 == 0 :
        j *= 2+1
    else:
        j *= 3
    print(i,j)