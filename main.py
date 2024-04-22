def counter(words):
    hashMap = {}
    for char in words:
        lower = char.lower()
        if lower.isalpha():
            if lower not in hashMap:
                hashMap[lower] = 1
            else:
                hashMap[lower] += 1
    return hashMap

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        words = f.read()
        print("-- Begin report of books/frankenstein.txt --")
        print(f"{len(words.split())} words found in the document")
        print("")
        charCount = counter(words)
        for char in sorted(charCount, reverse=True, key=charCount.get):
            print(f"the '{char}' character was found {charCount[char]} times")
        print(f"--- End report ---")

main()
