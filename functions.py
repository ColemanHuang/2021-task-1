import re


def get_text():
    file = open("test.c", "r", encoding="UTF-8")
    txt = file.read()
    for ch in '!#$%&()+,-.:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    # 考虑注释不算在内，不能去掉符号 * /
    # 考虑 "..." 引号之间不作为关键字
    file.close()
    return txt


keyWords = {"auto", "break", "case", "char", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return",
            "short", "signed", "sizeof", "static", "struct",
            "switch", "typedef", "union", "unsigned",
            "void", "volatile", "while", "elseif"}


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


def first_level():  # 统计关键字个数
    counts = {}
    cnt = 0
    for word in words:
        if len(word) == 1 or (word not in keyWords):
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
    return counts.get("switch", 0), count


def last_level():
    # print(filterWords)
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
    print("if-elseif-else num: {}".format(if_elseif_else_num))
    return if_else_num, if_elseif_else_num
