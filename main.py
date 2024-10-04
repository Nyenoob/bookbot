from pathlib import Path
from typing import Dict, Optional

def get_book_text(path):
#book_path = Path(__file__).parent / "books/frankenstein.txt"
#with open(book_path) as f:
    with open(path) as f:
        return f.read()

def get_Number_of_words(text):
    allthewords = text.split()
    return len(allthewords)

def convert_lower(text):
    return text.lower()

def count_chars(text):
    from collections import defaultdict
    char_count = defaultdict(int)
    sign_count = defaultdict(int)
    for char in text:
        if char.isalpha():
            char_count[char]+=1
        else:
            sign_count[char]+=1
    return char_count,sign_count   

def sort_dict(input_dict: Dict[str, int], sort_by: Optional[str] = "Value", order: Optional[str] = 'descending') -> Dict[str, int]:
    reverse_order = True if order == 'descending' else False
    if sort_by != "Value":
        sorted_items = sorted(input_dict.items(), key=lambda item: item[0], reverse=reverse_order)
    else:
        sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=reverse_order)
    sorted_dict = dict(sorted_items) 
    return sorted_dict

def main():
    booktitle = "frankenstein"
    path = "books/"+booktitle+".txt"
    text = get_book_text(path)
    text_lower=convert_lower(text)
    num_words = get_Number_of_words(text_lower)
    char_count,sign_count = count_chars(text_lower)
    sorted_char_count=sort_dict(char_count)
    print(f"--- This begins the report on {booktitle} ---")
    print(f"A total of {num_words} words found")
    #print(sorted_char_count)
    for entry in sorted_char_count:
        print(f"The '{entry}' character was found: {sorted_char_count[entry]} times")
    print(f"--- This ends the report on {booktitle} ---")

if __name__ == "__main__":
     main()
     
