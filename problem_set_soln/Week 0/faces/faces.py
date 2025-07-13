def convert(str):
    str = (str.replace(":)", "🙂", -1)).replace(":(", "🙁", -1)
    return str


def main():
    str = input()
    print(convert(str))

main()
