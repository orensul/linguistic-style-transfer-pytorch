import re
import logging
from linguistic_style_transfer_pytorch.config import GeneralConfig

config = GeneralConfig()


class Preprocessor():
    """
    Preprocessor class
    """

    def __init__(self):

        print("Preprocessor instantiated")

    def _clean_text(self, string):
        """
        Clean the raw text file
        """
        string = string.replace(".", "")
        string = string.replace(".", "")
        string = string.replace("\n", " ")
        string = string.replace(" 's", " is")
        string = string.replace("'m", " am")
        string = string.replace("'ve", " have")
        string = string.replace("n't", " not")
        string = string.replace("'re", " are")
        string = string.replace("'d", " would")
        string = string.replace("'ll", " will")
        string = string.replace("\r", " ")
        string = string.replace("\n", " ")
        string = re.sub(r'\d+', "number", string)
        string = ''.join(x for x in string if x.isalnum() or x == " ")
        string = re.sub(r'\s{2,}', " ", string)
        string = string.strip().lower()

        return string

    def preprocess(self):
        """
        Preprocesses the train text data 
        """
        print("Preprocessing started")
        with open(config.train_text_file_path, 'w') as text_file, open(config.train_labels_file_path, 'w') as labels_file:
            with open(config.train_pos_reviews_file_path, 'r') as reviews_file:
                for line in reviews_file:
                    line = self._clean_text(line)
                    if len(line) > 0:
                        text_file.write(line + "\n")
                        labels_file.write("pos" + "\n")
            with open(config.train_neg_reviews_file_path, 'r') as reviews_file:
                for line in reviews_file:
                    line = self._clean_text(line)
                    if len(line) > 0:
                        text_file.write(line + "\n")
                        labels_file.write("pos" + "\n")
        print("Processing complete ")



if __name__ == "__main__":
    prep = Preprocessor()
    prep.preprocess()