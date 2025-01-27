def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase 
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    for word, count in word_count.items():
        print(f"{word}: {count}")
main()