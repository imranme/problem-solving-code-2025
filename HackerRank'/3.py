def split_and_join(line):
    split = line.split(" ")
    join = "-".join(split)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


    problem link :https://www.hackerrank.com/challenges/python-string-split-and-join/problem1