# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_list = list(set(arr))
    unique_list.sort(reverse=True)
    if len(unique_list) >= 2:
        print(unique_list[1])
    else:
        print(unique_list[0])