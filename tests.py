import unittest
from format_price import format_price


class FormatPriceCase(unittest.TestCase):
    def test_1(self):
        price = format_price(" 123.40000 ")
        self.assertEqual(price, "123.40")

    def test_2(self):
        price = format_price("  1120.409892376 ")
        self.assertEqual(price, "1 120.41")

    def test_3(self):
        price = format_price("     .000001 ")
        self.assertEqual(price, "0.00")

    def test_4(self):
        price = format_price("112З.40000 \n")
        self.assertEqual(price, None)

    def test_5(self):
        price = format_price(" \n111123.40888\n ")
        self.assertEqual(price, "111 123.41")

    def test_6(self):
        price = format_price(" \n.40888\n ")
        self.assertEqual(price, "0.41")

    def test_7(self):
        price = format_price(" \n12.\n ")
        self.assertEqual(price, "12.00")

    def test_8(self):
        price = format_price(" \n12\n ")
        self.assertEqual(price, "12.00")

    def test_9(self):
        price = format_price("  . \n")
        self.assertEqual(price, None)

    def test_10(self):
        price = format_price(123.45)
        self.assertEqual(price, None)

    def test_11(self):
        price = format_price(['0.1', '1.2'])
        self.assertEqual(price, None)

    def test_12(self):
        price = format_price(None)
        self.assertEqual(price, None)

    def test_13(self):
        price = format_price(self.test_1)
        self.assertEqual(price, None)

    def test_14(self):
        price = format_price(self)
        self.assertEqual(price, None)

if __name__ == '__main__':
    unittest.main()
