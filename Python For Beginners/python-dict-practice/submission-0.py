from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = {}
    for char in word:
        counter = 0
        for i in word:
            if i == char:
                counter += 1
        my_dict[char] = counter
        counter = 0
    return my_dict








# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
