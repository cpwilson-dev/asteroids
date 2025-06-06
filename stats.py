def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    word_array = text.split()
    return len(word_array)

def get_character_count(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    
    return characters

def sort_character_count(dict_characters):
    return dict(sorted(dict_characters.items()))




