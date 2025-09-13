# https://www.hackerrank.com/challenges/python-tuples/problem 

# i went to solved this problem but some error heer 


if __name__ == '__main__':
    # প্রথম লাইনে n পড়ে নাও
    n = int(input())
    
    # দ্বিতীয় লাইনে nটি space-separated integers পড়ে tuple-এ কনভার্ট করো
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    
    # tuple-এর hash value প্রিন্ট করো
    print(hash(t))
