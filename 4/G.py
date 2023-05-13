# t = int(input())
# for i in range(t):
#     a = input()
#     if len(a) != 1:
#
#         if a[:len(a) // 2 - 1:] == a[len(a) // 2: -1:]:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")


def get_result(s: str):
    slice = len(s) // 2
    if s[:slice] == s[slice:]:
        return 'YES'
    return 'NO'


def main():
    for _ in range(int(input())):
        print(get_result(input()))


if __name__ == '__main__':
    main()
