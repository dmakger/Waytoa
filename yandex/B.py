import datetime
from decimal import Decimal

QUARTER_END = [3, 6, 9, 12]
YEAR = 2022


def get_need_quarter(start: list, end: list):
    first = start[1] // 3
    if start[1] % 3 != 0:
        first += 1
    finish = end[1] // 3
    if end[1] % 3 != 0:
        finish += 1
    return list(range(first, finish + 1))


def format_price(price, count_symbol: int = 2):
    if type(price) == int:
        price = float(price)
    return float(f"{int(price)}.{str(price).split('.')[1][:count_symbol]}")


def diff_date(start: list, end: list):
    return (datetime.datetime(end[0], end[2], end[1]) - datetime.datetime(start[0], start[2], start[1])).days


def get_valid_data(amount: str, date_from: str, date_finish: str):
    amount = int(amount)
    date_from = [int(x) for x in date_from.split('.')]
    date_finish = [int(x) for x in date_finish.split('.')]
    days = diff_date([YEAR, *date_from], [YEAR, *date_finish]) + 1
    price = amount / days
    return {
        'date_from': date_from,
        'date_finish': date_finish,
        'price': format_price(price),
        'quarter': get_need_quarter(date_from, date_finish),
    }


def get_start_end(quarter: int):
    start = [YEAR, 1, quarter * 3 - 2]

    end_mount = quarter * 3 + 1
    end_year = YEAR
    if end_mount == 13:
        end_mount = 12
        end_year += 1
    end = [end_year, 1, end_mount]
    return start, end


def main():
    result = [0, 0, 0, 0]
    for _ in range(int(input())):
        date = get_valid_data(*input().split())
        for i in range(len(date['quarter'])):
            start, end = get_start_end(date['quarter'][i])

            if date['quarter'][i] == date['quarter'][0]:
                start = [YEAR, *date['date_from']]
            if date['quarter'][i] == date['quarter'][-1]:
                end = [YEAR, *date['date_finish']]
                result[date['quarter'][i] - 1] += Decimal((diff_date(start, end) + 1) * date['price'])
                continue
            result[date['quarter'][i]-1] += Decimal(diff_date(start, end) * date['price'])

    for quarter in result:
        print(format(quarter, '.2f'))


if __name__ == '__main__':
    main()

# 4
# 10 10.02 11.05
# 10 11.12 23.12
# 100 24.05 30.06
# 4342 10.07 12.09
# 5.00
# 104.04
# 4342.00
# 9.88
