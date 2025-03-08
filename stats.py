def count_words(book_text):
    count = len(book_text.split())
    return count


def count_chars(book_text):
    chars_dict = {}
    for char in book_text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def most_common_char(input):
    character_dict = {}
    for char in input:
        char = char.lower()
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    most_common = ''
    highest_count = 0
    for char, count in character_dict.items():
        if count > highest_count:
            most_common = char
            highest_count = count

    return (most_common, highest_count)


def make_sorted_list(input):
    result = []
    for char, count in input.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)

    def sort_on(dict):
        return dict["count"]

    result.sort(reverse=True, key=sort_on)
    return result
