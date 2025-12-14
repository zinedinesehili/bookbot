def count_words(text):
    split_text = text.split()
    print(f"Found {len(split_text)} total words")

def num_characters(text):
    character_count = {}
    for char in text:
        lower = char.lower()
        if lower in character_count:
            character_count[lower] += 1
        else:
            character_count[lower] = 1
    return character_count

def sort_on(characters):
    return characters["num"]

def sort_dictionary(characters):
    list_of_dicts = []
    new_dict = {}
    for char in characters:
        new_dict = {"char":char, "num":characters[char]}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts