

X= int(input())


Sizes = list(map(int, input().split()))
inventory = Counter(Sizes)


N = int(input())


total_revenue = 0

for i in range(N):
    Shoe_size, Price = map(int, input().split())


    if inventory[Shoe_size] > 0:

        inventory[Shoe_size] -= 1
        total_revenue += Price


print(total_revenue)