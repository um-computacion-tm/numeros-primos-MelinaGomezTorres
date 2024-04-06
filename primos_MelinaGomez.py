import unittest

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        self.assertTrue(es_primo(2))

    def test_2(self):
        self.assertTrue(es_primo(3))

    def test_3(self):
        self.assertTrue(es_primo(5))

    def test_4(self):
        self.assertTrue(es_primo(7))

    def test_5(self):
        self.assertTrue(es_primo(11))

    def test_6(self):
        self.assertTrue(es_primo(13))

    def test_7(self):
        self.assertFalse(es_primo(1))

    def test_8(self):
        self.assertFalse(es_primo(4))

    def test_9(self):
        self.assertFalse(es_primo(6))

    def test_10(self):
        self.assertFalse(es_primo(8))

    def test_11(self):
        self.assertFalse(es_primo(9))

    def test_12(self):
        self.assertFalse(es_primo(10))

    def test_13(self):
        self.assertFalse(es_primo(12))

    def test_14(self):
        self.assertTrue(es_primo(9999999967))  # Número primo grande

    def test_15(self):
        self.assertFalse(es_primo(9999999968))  # Número compuesto grande

    def test_16(self):
        self.assertFalse(es_primo(-1032))

if __name__ == '__main__':
    unittest.main()
