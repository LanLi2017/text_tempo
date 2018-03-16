from nltk import word_tokenize
from nltk.corpus import stopwords
import re

doc1= open("religious-and-philosophical-texts/test.txt","r")
string=str(doc1.read())
print(string)
"""
word_tokenize
stop_words removal 
remove rege
"""
string_tokens=word_tokenize(string)
print(string_tokens)

clean_string=[word for word in string_tokens if word not in stopwords]

valid=re.compile(r"^[A-Za-z]\w+$")
string_valid=[valid.match(clean_string)]

"""
analysis each doc 
sentimental analyzer 
"""
