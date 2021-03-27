formatters = "plain bold italic header link inline-code ordered-list unordered-list new-line".split(" ")
string = []


def get_text():
    return input("Text: ")


def head():
    while 1:
        lvl = int(input("Level: "))
        if lvl in range(1, 7):
            break
        else:
            print("The level should be within the range of 1 to 6")
    txt = input("Text: ")
    return "#" * lvl + " " + txt + "\n"


def plain():
    return get_text()


def bold():
    return f"**{get_text()}**"


def italic():
    return f"*{get_text()}*"


def inline_code():
    return f"`{get_text()}`"


def new_line():
    return "\n"


def link():
    lbl = input("Label: ")
    url = input("URL: ")
    return f"[{lbl}]({url})"


def list_input(form):
    strn = []
    s = ''
    while 1:
        num = int(input("Number of rows: "))
        if num > 0:
            break
        else:
            print("The number of rows should be greater than zero")
    for n in range(0, num):
        strn.append(input(f"- Row #{n + 1}: ") + '\n')
    for i in range(num):
        if form == 'order':
            s = s + str(i + 1) + f'. {strn[i]}'
        elif form == 'unorder':
            s = s + f'* {strn[i]}'
    return s


def ordered_list():
    return list_input('order')


def unordered_list():
    return list_input('unorder')


def add_to_string(form):
    if form == 'header':
        return head()
    elif form == 'plain':
        return plain()
    elif form == 'bold':
        return bold()
    elif form == 'italic':
        return italic()
    elif form == 'link':
        return link()
    elif form == 'inline-code':
        return inline_code()
    elif form == 'new-line':
        return new_line()
    elif form == 'ordered-list':
        return ordered_list()
    elif form == 'unordered-list':
        return unordered_list()


def save():
    file = open('output.md', 'w')
    file.writelines(string)
    file.close()


def main():
    while True:
        formatter = input("- Choose a formatter: ")
        if formatter == "!help":
            print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
            Special commands: !help !done""")
        elif formatter in formatters:
            string.append(add_to_string(formatter))
        elif formatter == "!done":
            save()
            break
        else:
            print("Unknown formatting type or command. Please try again")
        print(*string, sep="")


if __name__ == '__main__':
    main()
