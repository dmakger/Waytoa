
def main():
    for _ in range(int(input())):
        digit = int(input())
        m = set()
        count = 1
        while count * count <= digit:
            m.add(count * count)
            count += 1

        count = 1
        while count * count * count <= digit:
            m.add(count * count * count)
            count += 1

        print(len(m))




if __name__ == '__main__':
    main()
