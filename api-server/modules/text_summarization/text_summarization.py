from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


class LexRank():
    def __init__(self):
        self.language = 'japanese'

    # lexrankをファイルを元に実行
    def lexrank_from_file(self, file, sentences_count=3):
        parser = PlaintextParser.from_file(file, Tokenizer(self.language))
        stemmer = Stemmer(self.language)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(self.language)
        result = ''
        for sentence in summarizer(parser.document, sentences_count):
            # print(sentence)
            result = result + str(sentence)
        return result

    # lexrankを文字列変数を元に実行
    def lexrank_from_string(self, content, sentences_count=3):
        parser = PlaintextParser.from_string(content, Tokenizer(self.language))
        stemmer = Stemmer(self.language)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(self.language)
        result = ''
        for sentence in summarizer(parser.document, sentences_count):
            # print(sentence)
            result = result + str(sentence)
        return result
