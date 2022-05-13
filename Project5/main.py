string_1 = input("Введите слова, разделяя их запятой: ")
words_1 = string_1.split(", ")

string_2 = input(f"Количество слов в списке: {len(words_1)}\nВведите столько же слов, разделяя их запятой: ")
words_2 = string_2.split(", ")

dct = {key: value for key, value in list(zip(words_1, words_2))}
print(dct)
