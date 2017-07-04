import sys

def format_price(price: "str") -> "str":
    try:
        price_float = float(price.strip())
    except ValueError:
        return "***.**"
    else:
        return "{:,.2f}".format(price_float).replace(',', ' ')


if __name__ == '__main__':
    print("{} converted to {}".format(sys.argv[1], format_price(sys.argv[1])))


