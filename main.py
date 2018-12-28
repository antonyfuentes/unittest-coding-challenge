import itertools
import os


class LargestWord:
    """
    Main program class.
    This class will allow you to load a file with text, then it will return the largest word
    As well as the same word in transposed form.
    """

    def __init__(self, file_path):
        """
        Constructor of the class
        :param file_path: path of the file to be loaded and processed
        """
        self.file_path = file_path

    def load_file(self):
        """
        Read file and return a flattened list of words
        :return: list object
        """
        try:
            with open(self.file_path, 'r') as f:

                if os.path.splitext(f.name)[1] != ".txt":
                    raise Exception('Invalid file type')

                file_lines = f.readlines()
                if len(file_lines) == 0:
                    raise Exception("File is empty")

                return [
                            i.strip() for i in itertools.chain.from_iterable(
                                [l.split() for l in file_lines]
                            )
                        ]
        except FileNotFoundError:
            return "File not found"
        except UnicodeDecodeError:
            return "File is corrupted"
        except Exception as error:
            return str(error)

    @staticmethod
    def largest_word(words):
        """
        Sort the list of words by their length and then return largest
        :param words: list of words to be sorted
        :return: string, largest word
        """

        if len(words) == 1:
            return "Found only 1 word"
        elif len(set(map(lambda w: len(w), words))) == 1:
            return "All words have the same length"
        elif len(words) == 0:
            return "There are no words"
        return sorted(words, key=len, reverse=True)[0]

    @staticmethod
    def transpose_word(word):
        """
        Transpose a given string
        :param word: String to be transposed
        :return: Transposed string
        """
        return word[::-1]


def main():
    """
    If someone executes this script in the __main__ scope,
    then an instance will be created with the default parameter below
    :return: NA
    """
    main_instance = LargestWord(file_path="tests/input_files/data_tc1.txt")
    words = main_instance.load_file()
    largest = main_instance.largest_word(words=words)
    transpose = main_instance.transpose_word(word=largest)

    print(largest)
    print(transpose)


if __name__ == "__main__":
    """
    Call main function is scrip is running on __main__ scope
    """
    main()
