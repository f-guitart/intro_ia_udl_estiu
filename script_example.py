# example from: https://cloud.google.com/natural-language/docs/quickstart-client-libraries#client-libraries-usage-python
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Hello, world!. I feel really good :)'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT,
    language="EN")

# check the document structure
print("-> Document structure:\n {}".format(document))

# Detects the sentiment of the text
response = client.analyze_sentiment(document=document, 
                                     encoding_type="UTF8")

#check the response structure
print("-> Response structure:\n {}".format(response))

print("---- Ouptut ----")
sentiment = response.document_sentiment
print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

