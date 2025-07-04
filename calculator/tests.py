from functions.get_file_content import get_file_content


def test():
    result = get_file_content(".", "main.py")
    print(result)

    result = get_file_content(".", "pkg/calculator.py")
    print(result)

    result = get_file_content(".", "/bin/cat")
    print(result)


if __name__ == "__main__":
    test()
