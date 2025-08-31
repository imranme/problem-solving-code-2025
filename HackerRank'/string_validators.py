#https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    s = input()
    operations = ["isalnum","isalpha","isdigit","islower","isupper"]
    for i in operations:
        print(any(getattr(c,i)() for c in s))