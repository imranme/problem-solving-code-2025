if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # দ্বিতীয় সর্বনিম্ন নাম্বার খুঁজে বের করো
    scores = sorted(set([s[1] for s in students]))
    second_lowest = scores[1]

    # যাদের নাম্বার দ্বিতীয় সর্বনিম্ন, তাদের নাম বের করো
    result_names = [s[0] for s in students if s[1] == second_lowest]
    
    # বর্ণানুক্রমে সাজিয়ে প্রিন্ট
    for name in sorted(result_names):
        print(name)


# https://www.hackerrank.com/challenges/nested-list/problem