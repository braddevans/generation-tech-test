def read_row(file):
    next_line = file.readline()

    if len(next_line) > 0:
        return __parse_row(next_line)

    return None


def __parse_row(next_line):
    # print(f"{next_line}")
    nextline = next_line.replace("\n", "")
    parsed_list = nextline.split(",")
    clean_list = []
    for key, value in enumerate(parsed_list):
        clean_list.append(value.replace('\"', ""))
    return clean_list
