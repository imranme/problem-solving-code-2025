# from collections import defaultdict  # defaultdict লাইব্রেরি ইমপোর্ট করলাম

# n, m = map(int, input().split())  # প্রথম লাইনে ২টি সংখ্যা ইনপুট নিচ্ছি (group A এর সংখ্যা এবং group B এর সংখ্যা)

# group_a = defaultdict(list)  # group A তৈরি করছি defaultdict দিয়ে, যাতে একাধিক ইনডেক্স লিস্ট আকারে রাখা যায়

# # group A এর n টি ইনপুট নেওয়া হবে
# for i in range(1, n + 1):  # ১ থেকে শুরু করছি কারণ ইনডেক্স ১-based হবে
#     word = input()  # শব্দ ইনপুট নিচ্ছি
#     group_a[word].append(i)  # সেই শব্দের জন্য ইনডেক্স লিস্টে যোগ করছি

# # group B এর m টি শব্দ ইনপুট নিচ্ছি
# for _ in range(m):
#     word = input()
#     if word in group_a:  # যদি group A তে এই শব্দ থাকে
#         print(' '.join(map(str, group_a[word])))  # তাহলে তার সব ইনডেক্স প্রিন্ট করো (স্পেস দিয়ে)
#     else:
#         print(-1)  # না থাকলে -1 প্রিন্ট করো


from collections import defaultdict 
n, m = map(int, input().split())

group_a = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

for _ in range(m):
    word = input()
    if word in group_a:
        for index in group_a[word]:
                print(index, end=' ')
        print()
    else:
        print(-1)