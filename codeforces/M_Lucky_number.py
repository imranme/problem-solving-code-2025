a, b = map(int, input("").split())

lucky =[]

for i in range(a,b+1):
    if all(ch in "47" for ch in str(i)):
        lucky.append(str(i))

if lucky:
    print(" ".join(lucky))
else:
    print("-1")
  