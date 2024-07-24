
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        char_count_list = []
        for c in char_count:
            char_count_list.append({"name":c, "num":char_count[c]})

        char_count_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("\n")
        for k in char_count_list:
            print(f"The '{k['name']}' character was found {k['num']} times")
        print("--- End report ---")

def count_words(str):
    words = str.split()
    return len(words)
    
def count_chars(str):
    freq_map = {}
    for c in str:
        if c.isalpha():
            cc = c.lower()
            if cc in freq_map:
                freq_map[cc] += 1
            else:
                freq_map[cc] = 1
    return freq_map

def sort_on(dict):
    return dict["num"]

main()