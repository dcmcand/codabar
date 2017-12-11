import argparse
import config

def generate_barcode():


    bar = input("Please enter a barcode: ")
    bar = str(bar)
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add-prefix", dest="prefix", nargs="?", const=True, help="Specifies whether or not to add a prefix. This option requires -p")
    parser.add_argument("-p", "--prefix-type", dest="ptype", choices=['book', 'card'], help="Specifies which type of prefix to add. Options are book or card")
    args = parser.parse_args()
    card_prefix = config.card_prefix
    book_prefix = config.book_prefix


    if args.prefix:
        if args.ptype:
            if args.ptype == "book":
                bar = book_prefix + bar
            elif args.ptype == "card":
                bar = card_prefix + bar
    return add_check_digit(bar)


def add_check_digit(bar):
    if bar.isdigit():
        barcode = bar
        odd_sum = 0
        even_sum = 0
        odds_greater_than_4 = 0
        for x in range(len(barcode)):
            if x % 2 == 0:
                odd_sum += int(barcode[x])
                if int(barcode[x]) > 4:
                    odds_greater_than_4 += 1
            else:
                even_sum += int(barcode[x])
            check_digit = 10 - (((odd_sum * 2) + even_sum + odds_greater_than_4) % 10)
            if check_digit == 10:
                check_digit = 0
        return str(bar) + str(check_digit)
    else:
        print("Card Number must be 13 or 14 digits long")


if __name__ == "__main__":
    print(generate_barcode())
