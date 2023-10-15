from nltk import sent_tokenize


def _split_sentences_ru(text, n=2):
    # Set the language to Russian for sentence tokenization
    res = sent_tokenize(text, language='russian')
    return " ".join(res[:n])
