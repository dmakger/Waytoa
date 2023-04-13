from math import ceil


def get_valid_height_image(s: str, width: int):
	r = [int(x) for x in s.split('x')]
	return ceil((r[1] * width) / r[0])


def main():
	w = int(input())
	n, k = map(int, input().split())
	height_all = sorted(get_valid_height_image(input(), w) for _ in range(n))
	print(sum(height_all[:k]))
	print(sum(height_all[-k:]))



if __name__ == '__main__':
	main()
