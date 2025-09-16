def get_word_count(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_character_count(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def helper(dict):
    return dict["num"]

def sort_dict(dict):
    list = []

    for key in dict:
        list.append({"char": key, "num": dict[key]})
    
    list.sort(reverse=True, key=helper)
    
    return list