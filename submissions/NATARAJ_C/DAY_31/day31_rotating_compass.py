list1=list(map(int,input("Enter numbers: ").split()))
k=int(input("Enter rotation value(k): "))
k=k%len(list1)
rotated_list=list1[k:]+list1[:k]
print("Rotated list:",*rotated_list)