def count_substring(string, sub_string):
    size = len(sub_string)
    s = ""
    count = 0
    for i in range(0, size):
        s += string[i]
    if s == sub_string:
        count += 1
    for i in range(size, len(string)):
        s = s[1:] + string[i]
        if s == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input("Enter main string: ")
    sub_string = input("Enter sub string: ")
    result = count_substring(string, sub_string)
    print(result)
