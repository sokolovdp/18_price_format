# Price Formatter
Function **format_price(price: str) -> str:** converts string with float number to currency format with space grouping
In case of format error in input string (chars instead of digits) function returns **None** object.
# CLI usage
```
python.exe format_price.py 1234.56789
1234.56789 converted to 1 234.57
```
```
python.exe format_price.py 12A.56
12A.56 converted to None
```
# Unit tests
To automatically check format_price(price: "str") function run test.py script, which applies 9 checks
```
python.exe tests.py
.........
----------------------------------------------------------------------
Ran 14 tests in 0.000s

OK

Process finished with exit code 0
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
