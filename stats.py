
def get_file_contents(resources_path):

    with open(resources_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_contets):

    return len(file_contets)

def get_num_char(file_contets):
    lower_contets = file_contets.lower()
    char_dict ={}
    for char in lower_contets:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    print_dictionary(char_dict)


def print_dictionary(char_dict):
    for key in char_dict:
        if key.isalpha():
            print(f"{key} --> {char_dict[key]}")
