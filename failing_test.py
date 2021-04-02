import unittest
import failing

class FailingTests(unittest.TestCase):

    def testFailing(self):
        with self.assertRaises(Exception) as context:
            failing.failing()

        exceptionMessage = "There's something happening here. But what it is ain't exactly clear!"
        exception = context.exception
        self.assertEqual(exceptionMessage, str(exception))

