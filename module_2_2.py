int1=int(input("first ="))
int2=int(input("second ="))
int3=int(input("third ="))
if int1==int2 and int1==int3 and int2==int3:
    print(3)
elif int1==int2 or int1==int3 or int2==int3:
    print(2)
else:
    print(0)

