# import libraries
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
summarizer_lex = LexRankSummarizer()

# getting data
text = """Text summarization is the practice of breaking down long publications into manageable paragraphs or sentences. 
The procedure extracts important information while also ensuring that the paragraph's sense is preserved.
This shortens the time it takes to comprehend long materials like research articles while without omitting critical information.
The process of constructing a concise, cohesive, and fluent summary of a lengthier text document, which includes highlighting the
text's important points, is known as text summarization. Text summarising presents a number of issues, including text identification, 
interpretation, and summary generation, as well as analysis of the resulting summary. Identifying important phrases in the document 
and exploiting them to uncover relevant information to add in the summary are critical jobs in extraction-based summarising."""

# parsing from string
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Summarize using sumy LexRank. Unsupervized approach 
summary= summarizer_lex(parser.document, 5)
lex_summary=""
for sentence in summary:
    lex_summary+=str(sentence)
    # print(lex_summary)
print(len(lex_summary))

