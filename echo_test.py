import unittest
import echo

class EchoTests(unittest.TestCase):

    def testEcho(self):
        self.assertFail("This is a failing test...")
#        expected = "TEST MESSAGE"
#        result = echo.echo(expected)
#        self.assertEqual(expected, result)
