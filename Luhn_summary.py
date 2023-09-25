# Using Luhn package from Sumy to sammarize text
# import libraries
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
# based on frequency of most important words

# get data
text = """Text summarization is the practice of breaking down long publications into manageable paragraphs or sentences. 
The procedure extracts important information while also ensuring that the paragraph's sense is preserved.
This shortens the time it takes to comprehend long materials like research articles while without omitting critical information.
The process of constructing a concise, cohesive, and fluent summary of a lengthier text document, which includes highlighting the
text's important points, is known as text summarization. Text summarising presents a number of issues, including text identification, 
interpretation, and summary generation, as well as analysis of the resulting summary. Identifying important phrases in the document 
and exploiting them to uncover relevant information to add in the summary are critical jobs in extraction-based summarising."""

# parsing from string
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Luhn Summarizer
luhn_summarizer = LuhnSummarizer()

# summary
summary = luhn_summarizer(parser.document, 5)

luhn_summary=""
for sentence in summary:
    luhn_summary+=str(sentence)
    # print(lex_summary)
print(len(luhn_summary))
