
def count_words(text):
    words = len(text.split())
    return(words)

def count_chars(text):
    chars_count = {}
    for char in text.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_on(letters):
    return letters["count"]

def sort_chars(char_dict):
    characters = []
    for item in char_dict:
        characters.append({"char":item, "count":char_dict[item]})
    characters.sort(reverse=True, key=sort_on)
    return characters

