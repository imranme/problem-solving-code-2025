if __name__ == '__main__':
    N = int(input())  # মোট কতটি কমান্ড আছে
    my_list = []      # খালি লিস্ট

    for _ in range(N):
        cmd = input().split()  # প্রতিটি কমান্ডকে শব্দে ভাঙো
        command = cmd[0]       # যেমন: insert, append
        args = cmd[1:]         # বাকি অংশ যেমন index, value

        if command == "print":
            print(my_list)
        else:
            # getattr দিয়ে সরাসরি কমান্ড চালানো
            getattr(my_list, command)(*map(int, args))
