import unittest
import echo

class EchoTests(unittest.TestCase):

    def testEcho(self):
        expected = "TEST MESSAGE"
        result = echo.echo(expected)
        self.assertEqual(expected, result)
