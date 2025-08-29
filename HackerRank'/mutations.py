# link: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    # একে slice বা list যেকোনো পদ্ধতি দিয়ে করো
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()              # প্রথম লাইন: স্ট্রিং
    i, c = input().split()   # দ্বিতীয় লাইন: index এবং character
    s_new = mutate_string(s, int(i), c)
    print(s_new)
