import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

# text 
text = """Text summarization is the practice of breaking down long publications into manageable paragraphs or sentences. 
The procedure extracts important information while also ensuring that the paragraph's sense is preserved.
This shortens the time it takes to comprehend long materials like research articles while without omitting critical information.
The process of constructing a concise, cohesive, and fluent summary of a lengthier text document, which includes highlighting the
text's important points, is known as text summarization. Text summarising presents a number of issues, including text identification, 
interpretation, and summary generation, as well as analysis of the resulting summary. Identifying important phrases in the document 
and exploiting them to uncover relevant information to add in the summary are critical jobs in extraction-based summarising."""

print('Length of Original document')
print(len(text))
# checking stopwords length

stopwords = list(STOP_WORDS)
print(len(stopwords))

# import english models
nlp = spacy.load("en_core_web_sm")
docx = nlp(text)

# # Finding number of sentence
# print(list(docx.sents))

keywords = []
# getting stopwords
stopwords = list(STOP_WORDS)
pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
for token in docx:
    if(token.text in stopwords or token.text in punctuation):
        continue
    if(token.pos_ in pos_tag):
        keywords.append(token.text)

# calculating frequency
freq_word = Counter(keywords)
print(freq_word.most_common(5))  # getting top five common words

# normalizing frequency
max_freq = Counter(keywords).most_common(1)[0][1]
for word in freq_word.keys():
    freq_word[word] = (freq_word[word]/ max_freq)

# normalized list
print(freq_word.most_common(5))

# weighing sentences
sent_strength = {}
for sent in docx.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if word in sent_strength.keys():
                sent_strength[sent]+= freq_word[word.text]
            else:
                sent_strength[sent]= freq_word[word.text]
print(sent_strength)

# summarizing
summarized_text = nlargest(3, sent_strength, key=sent_strength.get)

# converting to string
final_sentences  = [w.text for w in summarized_text]
summary = ' '.join(final_sentences)
print()
print()
print('After Summarizing')
print(len(summary))