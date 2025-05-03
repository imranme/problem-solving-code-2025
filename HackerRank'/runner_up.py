if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        sArr = sorted(arr)          #sort it first
        newL = list(set(sArr))     #then remove the duplicates
        print(newL[-2])              #then print the second one
