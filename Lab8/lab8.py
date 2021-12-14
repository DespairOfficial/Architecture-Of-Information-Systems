import string 

dictionary = {'молоко': 'milk', 'машина' : 'car', 'снег':'snow'}
def engToRu():
    reversedDictionary = {dictionary[a]: a for a in dictionary}
    if(word in reversedDictionary):
        print(str(word) + " - " + str(reversedDictionary[word]))    
    else:
       option =  input("Это слово ещё не в словаре, хотите его добавить? y/n: ")
       if(option == "N" or option == "n"):
           pass
       if (option == "Y" or option == "y"):
           newWord = input("Введите перевод слова: ")
           dictionary[newWord] = word
def ruToEng():
    if(word in dictionary):
        print(str(word) + " - " + str(dictionary[word]))
    else:
       option =  input("Это слово ещё не в словаре, хотите его добавить? y/n: ")
       if(option == "N" or option == "n"):
           pass
       if (option == "Y" or option == "y"):
           newWord = input("Введите перевод слова: ")
           dictionary[word] = newWord
while True:
    word = input("Перевести: ")
    if(word[0] in string.ascii_letters):
        engToRu()
    else:
        ruToEng()

    
        