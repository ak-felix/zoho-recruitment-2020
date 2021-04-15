str=input("string:")
len=len(str)
for i in range(len):
    for j in range(len-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(str[j],end=" ")
    print()
