from unittest import TestCase
from main import LargestWord


class MainPositiveTest(TestCase):

    def test_tc1(self):
        """
        Happy path test case.
        Validate that largest word is 'abcde' and that transposed equals to 'edcba'.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc1.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)
        transposed = tc.transpose_word(word=largest)

        self.assertEqual('abcde', largest)
        self.assertEqual('edcba', transposed)

    def test_tc1_2(self):
        """
        Validate that the largest word is not equal to the transposed word.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc1.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)
        transposed = tc.transpose_word(word=largest)

        self.assertNotEqual(largest, transposed)

    def test_tc2(self):
        """
        Validate program against file that contains multiple words in a single line.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc2.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)
        transposed = tc.transpose_word(word=largest)

        self.assertEqual('consectetuer', largest)
        self.assertEqual('reutetcesnoc', transposed)

    def test_tc3(self):
        """
        Validate program against file that contains multiple lines and multiple words per line.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc3.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)
        transposed = tc.transpose_word(word=largest)

        self.assertEqual('vulputate-eleifend', largest)
        self.assertEqual('dnefiele-etatupluv', transposed)

    def test_tc4(self):
        """
        Validate program against file that contains all words of the same length.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc4.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)

        self.assertEqual('All words have the same length', largest)

    def test_tc5(self):
        """
        Validate program against file that contains all words of type number.
        """
        tc = LargestWord(file_path="tests/input_files/data_tc5.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)
        transposed = tc.transpose_word(word=largest)

        self.assertEqual('0000001', largest)
        self.assertEqual('1000000', transposed)
