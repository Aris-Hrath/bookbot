def word_count(book):
    return len(book.split())

def letter_count(book):
    diction = {}
    for letter in book:
        lower = letter.lower()
        if lower in diction:
            diction[lower] += 1
        else:
            diction[lower] = 1
    return diction

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sorted_list(letter_w_counts: dict[str, int]) -> list[dict]:
    result = []
    for ch, n in letter_w_counts.items():
        result.append({"char": ch, "num": n})
    result.sort(reverse=True, key=sort_on)
    return result