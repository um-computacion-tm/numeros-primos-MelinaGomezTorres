import unittest

def is_primo(value):
    if value <= 1:
        return False
    elif value <= 3:
        return True
    elif value % 2 == 0 or value % 3 == 0:
        return False
    i = 5
    while i * i <= value:
        if value % i == 0 or value % (i + 2) == 0:
            return False
        i += 6
    return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_60(self):
        result = is_primo(60)
        self.assertEqual(result, False)

    def test_1049(self):
        result = is_primo(1049)
        self.assertEqual(result, True)
    
    def test_1069(self):
        result = is_primo(1069)
        self.assertEqual(result, True)

    def test_num_negativo(self):
        result = is_primo(-20)
        self.assertEqual(result, False)

    def test_num3_negativo(self):
        result = is_primo(-105)
        self.assertEqual(result, False)

    def test_num4_negativo(self):
        result = is_primo(-1032)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()