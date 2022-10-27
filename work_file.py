from log_decorator import log_decorator


def read_file():
    with open('bd', 'r') as file:
        with open('clean_bd', 'at+') as clean_file:
            for line in file.readlines():
                line = line.replace('{', '').replace('}', '').replace(',', '').replace("'name'", '').replace("'phone'",
                                                                                                             '').replace(
                    ':', '')
                clean_file.write(line)


@log_decorator
def main() -> None:
    read_file()


if __name__ == '__main__':
    main()
