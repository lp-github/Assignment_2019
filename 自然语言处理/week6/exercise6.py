def tokenize(word):
    import nltk
    words = nltk.word_tokenize(word)
    tags = nltk.pos_tag(words)
    print(tags)
def parse(word):
    import nltk
    grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> VBD NP | VBD NP PP
    PP -> IN NP
    NP -> DT NN|DT NN PP
    DT -> "the"|"a"
    NN -> "boy"|"dog"|"rod"
    VBD -> "saw"
    IN -> "with"
    """)
    words = nltk.word_tokenize('the boy saw the dog with a rod')
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for tree in rd_parser.parse(words):
        print(tree)
def main():
    words1 = "the lawyer questioned the witness about the revolver"
    words2 = "the boy saw the dog with a rod"
    tokenize(words1)
    parse(words2)
main()
import time
time.sleep(5)