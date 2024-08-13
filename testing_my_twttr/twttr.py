# twttr.py

def shorten(word):
    letter = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in letter:
        word = word.replace(i, "")
    return word

def main():
    word = input("Input: ")
    print(shorten(word))

if __name__ == "__main__":
    main()
