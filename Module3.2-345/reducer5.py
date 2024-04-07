import sys
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
import re

def clean(input_string):
    pattern = r'[^a-zA-Z\s]' 
    cleaned_string = re.sub(pattern, '', input_string)
    return cleaned_string

def find_most_similar_country(country_name, mydict):
    reference_set = set(mydict[country_name])
    similarities = {}
    for name, value in mydict.items():
        if name != country_name:
            jaccard_sim = jaccard_similarity(reference_set, set(value))
            similarities[name] = jaccard_sim
    print(similarities)
    most_similar_country = max(similarities, key=similarities.get)
    max_similarity = similarities[most_similar_country]
    return most_similar_country, max_similarity

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)


name=sys.argv[1]
country_name=name.lower()

mydict={'australia':[],'india':[],'england':[],'singapore':[],'malaysia':[]}

for line in sys.stdin:
    line=line.strip()
    line=line.split(':')

    text=remove_stopwords(line[2])
    cleantext=clean(text)
    cleantext=cleantext.split()
    for i in cleantext:
        mydict[line[0]].append(i)

similar_country,similarity_score=find_most_similar_country(country_name,mydict)
print(similar_country,similarity_score)

    