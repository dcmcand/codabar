import argparse
import config

def generate_barcode():




    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add-prefix", dest="prefix", default=False, nargs="?", const=True, help="Specifies whether or not to add a prefix. This option requires -p")
    parser.add_argument("-b", "--barcode", dest="barcode", help="Allows specifying barcode from the command line. If not set, user will be prompted for a barcode")
    parser.add_argument("-p", "--prefix-type", dest="ptype", choices=config.prefixes.keys(), help="Specifies which type of prefix to add.")
    args = parser.parse_args()




    if not args.barcode:
        bar = input("Please enter a barcode: ")
    else:
        bar = args.barcode

    if args.prefix:
        prefix = config.prefixes[args.ptype]
        bar = prefix + bar
    return add_check_digit(bar)


def add_check_digit(bar):
    if bar.isdigit():
        odd_sum = 0
        even_sum = 0
        odds_greater_than_4 = 0
        for x in range(len(bar)):
            if x % 2 == 0:
                odd_sum += int(bar[x])
                if int(bar[x]) > 4:
                    odds_greater_than_4 += 1
            else:
                even_sum += int(bar[x])
            check_digit = 10 - (((odd_sum * 2) + even_sum + odds_greater_than_4) % 10)
            if check_digit == 10:
                check_digit = 0
        return bar + str(check_digit)


if __name__ == "__main__":
    print(generate_barcode())
