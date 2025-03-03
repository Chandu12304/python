n=int(input("Enter the size of the list: "))
num_list=[int(input(f"Enter the element {i+1}: "))for i in range(n)]

l,m,h=0,-1,n-1
k=int(input("Enter the key element: "))

while (l<=h):
    m=(l+h)//2
    if(num_list[m]==k):
        break
    elif(num_list[m]<k):
        l=m+1
    else:
        h=m-1
if(m==-1):
    print("Element not found")
else:
    print(f"Element found at index {m}")
        
