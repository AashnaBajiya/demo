import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
© 2021 GitHub, Inc.
