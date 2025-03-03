st = input("Enter the string: ")
my_set=set(st)
for c in my_set:
    print(f"{c}: {st.count(c)}")
