def word_count(book_content):
    words = str.split(book_content)
    return len(words)

def unique_char_count(book_content):
    chars = {}
    for char in book_content.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    # print(dict)
    return dict["count"]

def sort_by_most(char_dict):
    dict_keys = char_dict.keys()
    # print(len(dict_keys))
    dict_list = []
    for key in dict_keys:
        dict_list.append({ "char": key, "count": char_dict[key]})
    # print(dict_list)    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list