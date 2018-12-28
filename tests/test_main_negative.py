from unittest import TestCase
from main import LargestWord


class MainNegativeTest(TestCase):
    """
    Negative tests to be executed against LargestWord
    """

    def test_tc6(self):
        """
        Validate program against file that doesn't contain any words, only contains spaces and tabs
        """
        tc = LargestWord(file_path="tests/input_files/data_tc6.txt")
        words = tc.load_file()
        largest = tc.largest_word(words=words)

        self.assertEqual('There are no words', largest)

    def test_tc7(self):
        """
        Validate program against empty file
        """
        tc = LargestWord(file_path="tests/input_files/data_tc7.txt")

        self.assertEqual('File is empty', tc.load_file())

    def test_tc8(self):
        """
        Validate program against non-existing file
        """
        tc = LargestWord(file_path="tests/input_files/data_non_existing_file.txt")

        self.assertEqual("File not found", tc.load_file())

    def test_tc9(self):
        """
        Validate program against invalid file type
        """
        tc = LargestWord(file_path="tests/input_files/data_tc9.jpg")

        self.assertEqual("Invalid file type", tc.load_file())

    def test_tc10(self):
        """
        Validate program against a corrupted file
        Note:
            Generated file using command: dd if=/dev/urandom of=data_tc10.txt bs=5000 count=1
        """
        tc = LargestWord(file_path="tests/input_files/data_tc10.txt")

        self.assertEqual("File is corrupted", tc.load_file())
