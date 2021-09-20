import sys
import re


def get_text():
    file = open(sys.argv[1], "r", encoding="UTF-8")
    txt = file.read()
    for ch in '!#$%&()+,-.:;<=>?@[\\]^_{|}~':
        # 考虑注释和引号，不能去掉符号 * / “
        txt = txt.replace(ch, " ")
    file.close()
    return txt


def words_filter():
    txt = get_text().replace("else if", "elseif")
    separator = [r'//.*', r'\/\*(?:[^\*]|\*+[^\/\*])*\*+\/', r'".*"']
    # 分别去掉 //单行注释  /* 多行注释*/  "引号"
    for sp in separator:
        wordlist = re.split(sp, txt)
        txt = ""
        for word in wordlist:
            txt = txt + word
    wordlist = txt.split()
    return wordlist


words = words_filter()
filterWords = []


def first_level():
    # 统计关键字个数
    keywords = {"auto", "break", "case", "char", "const",
                "continue", "default", "do", "double", "else",
                "enum", "extern", "float", "for", "goto",
                "if", "int", "long", "register", "return",
                "short", "signed", "sizeof", "static", "struct",
                "switch", "typedef", "union", "unsigned",
                "void", "volatile", "while", "elseif"
                }
    counts = {}
    cnt = 0
    for word in words:
        if len(word) == 1 or (word not in keywords):
            continue
        counts[word] = counts.get(word, 0) + 1
        filterWords.append(word)
        cnt = cnt + 1
    cnt = cnt + counts.get("elseif", 0)  # elseif 合并后要多算一次
    print("total num: {}".format(cnt))
    return counts


def second_level(counts):
    num = counts.get("switch", 0)
    print("switch num: {}".format(num))
    if num == 0:
        print("case num: {}".format(num))
        return
    count = []
    flag = -1
    for word in words:
        if word == "switch":
            count.append(0)
            flag += 1
        elif word == "case":
            count[flag] += 1
        else:
            continue
    print("case num: ", end="")
    print(" ".join(str(x) for x in count))


def last_level():
    stack = []
    if_else_num = 0
    if_elseif_else_num = 0
    for word in filterWords:
        if word == "if":
            stack.append(word)
        elif word == "elseif" and stack[-1] != "elseif":
            stack.append(word)
        elif word == "else":
            if stack[-1] == "if":
                stack.pop()
                if_else_num += 1
            elif stack[-1] == "elseif":
                stack.pop()
                stack.pop()
                if_elseif_else_num += 1
    print("if-else num: {}".format(if_else_num))
    if sys.argv[2] == '4':
        print("if-elseif-else num: {}".format(if_elseif_else_num))


def main():
    if '1' <= sys.argv[2] <= '4':
        counts = first_level()
    if '2' <= sys.argv[2] <= '4':
        second_level(counts)
    if '3' <= sys.argv[2] <= '4':
        last_level()


main()
