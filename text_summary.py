from gensim.summarization import summarize
import csv

# text 
text = """Text summarization is the practice of breaking down long publications into manageable paragraphs or sentences. 
The procedure extracts important information while also ensuring that the paragraph's sense is preserved.
This shortens the time it takes to comprehend long materials like research articles while without omitting critical information.
The process of constructing a concise, cohesive, and fluent summary of a lengthier text document, which includes highlighting the
text's important points, is known as text summarization. Text summarising presents a number of issues, including text identification, 
interpretation, and summary generation, as well as analysis of the resulting summary. Identifying important phrases in the document 
and exploiting them to uncover relevant information to add in the summary are critical jobs in extraction-based summarising."""

print(len(text))

summary_text = summarize(text)

print(type(summary_text))
print(len(summary_text))
# saving a file
with open('text_summary.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(summary_text)
# we can do two types of text summarization.
#  Summarizing with ratio default is 0.2 i.e 20%, ratio=0.5
# Summarizing with word count/ we can specify word_count = 50. So we will only get 50 words

#
