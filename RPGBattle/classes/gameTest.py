import unittest
from game import Person

class ClassesTest(unittest.TestCase):
    
    def test_PersonContructor(self):
        player = Person(460,65,60,34,'')
        self.assertEqual(460, player.hp)


if __name__ == '__main__':
    unittest.main()