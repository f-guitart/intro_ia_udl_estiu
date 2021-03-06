"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import six

def print_result(annotations, verbose):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    language = annotations.language

    spacing = ""
    if verbose:
        print("Detected Language: {}".format(language))
        spacing = "     "
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        sentence_magnitude = sentence.sentiment.magnitude
        if verbose:
            print("-> Sentence {}: {}".format(index, sentence.text.content))
        print('{}Sentence {} has a sentiment score of {}'.format(
            spacing, index, sentence_sentiment))
        if verbose:
            print('{}Sentence {} has a sentiment magintude of {}'.format(
            spacing, index, sentence_magnitude))

    print('** Overall Sentiment: score of {} with magnitude of {} **'.format(
        score, magnitude))
    return 0


def classify_text(text):
    """Classifies content categories of the provided text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Text sentiment analyzer",
        description="The program analyzes the text passed",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-v", "--verbose",
        help="increase output verbosity",
        action="store_true")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--text", 
        type=str, 
        help='The text you\'d like to analyze.',
        nargs='+')
    group.add_argument("-f", "--file", 
        type=str, 
        help='The text you\'d like to analyze.')

    args = parser.parse_args()
    verbose = args.verbose

    if args.text is not None:
        input_text = " ".join(args.text)

    if args.file is not None:
        input_file = args.file
        with open(input_file, "r") as f:
            input_text = f.read()
    
    classify_text(input_text)
