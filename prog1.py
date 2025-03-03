n= int(input("enter the size of the list "))
num_list = [0]*n
for i in range(n):
    num_list[i]=int(input("Enter elemnt "+ str(i+1) + ":"))

for el in num_list:
    if (el*el)%8==0:
        print(el)
