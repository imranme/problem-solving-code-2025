n = input().strip()

# reverse and remove leading zeros
reversed_n = n[::-1].lstrip("0")
print(reversed_n)

# check palindrome
if n == n[::-1]:
    print("YES")
else:
    print("NO")
