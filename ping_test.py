import unittest
import ping

class PingTests(unittest.TestCase):

    def testPing(self):
        expected = "pong:TEST MESSAGE"
        message = "TEST MESSAGE"
        result = ping.ping(message)
        self.assertEqual(expected, result)
