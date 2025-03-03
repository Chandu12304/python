def mergeSort(low, high, num_list):
    if low >= high:
        return
    mid = (low + high) // 2  # // --> integer divison and / --> float divison 
    mergeSort(low, mid, num_list)
    mergeSort(mid + 1, high, num_list)
    merge(low, mid, high, num_list)

def merge(low, mid, high, num_list):
    list1 = num_list[low:mid + 1]
    list2 = num_list[mid + 1:high + 1]

    i, j, k = 0, 0, low
    n1, n2 = len(list1), len(list2)

    while i < n1 and j < n2: # && --> and in python
        if list1[i] < list2[j]:
            num_list[k] = list1[i]
            i += 1 # i++ will not work
        else:
            num_list[k] = list2[j]
            j += 1
        k += 1

    while i < n1:
        num_list[k] = list1[i]
        i += 1
        k += 1

    while j < n2:  
        num_list[k] = list2[j]
        j += 1
        k += 1

# Input Handling
n = int(input("Enter the size of the list: "))
num_list = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

mergeSort(0, n - 1, num_list)  

print("Sorted List:", num_list)
