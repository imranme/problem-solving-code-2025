# https://www.hackerrank.com/challenges/python-tuples/problem 

# i went to solved this problem but some error heer 


# if name == 'main':
#     # প্রথম লাইনে n পড়ে নাও
#     n = int(raw_input())
    
#     # দ্বিতীয় লাইনে nটি space-separated integers পড়ে tuple-এ কনভার্ট করো
#     # integer_list = map(int, input().split())
#     # t = tuple(integer_list)
#     elements = tuple(map(int, raw_input().split()))
#     print (hash(elements))

    
#     # tuple-এর hash value প্রিন্ট করো
#     # print(hash(t))

if __name__ == '__main__':
    n = int(input())                    # Python 3–এ raw_input নয়, input() ব্যবহার করো
    t = tuple(map(int, input().split()))  # space-separated integers কে tuple এ রূপান্তর
    print(hash(t))                      # tuple-এর hash value প্রিন্ট
