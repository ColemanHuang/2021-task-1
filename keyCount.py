import sys


def get_text():
    txt = open(sys.argv[1], "r").read()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    return txt


keyWords = {"auto", "break", "case", "char", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return",
            "short", "signed", "sizeof", "static", "struct",
            "switch", "typedef", "union", "unsigned",
            "void", "volatile", "while"}

codeTxt = get_text()
words = codeTxt.split()


def first_level():
    counts = {}
    cnt = 0
    for word in words:
        if len(word) == 1 or (word not in keyWords):
            continue
        counts[word] = counts.get(word, 0) + 1
        cnt = cnt + 1
    print("total num: {}".format(cnt))
    return counts


def main():
    if sys.argv[2] == '1':
        first_level()


main()
