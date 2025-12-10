# Count unique words exercise

text = "Python is great. Python is easy to learn."


def count_unique_words(text):
    result = {}

    clean_text = text.replace(".", "").replace(",", "").lower()
    textList = clean_text.split(" ")

    for word in textList:
        result[word] = result.get(word, 0) + 1
    return result


result = count_unique_words(text)
print(result)
print(result.get("test"))
