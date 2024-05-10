
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)

    print("--- Begin report of " + book_path + " ---")
    print(f"{num_words} words found in the document")

    letter_dict = count_letter(text)
    sorted_dict = []

    for key in letter_dict:
        sorted_dict.append({ "letter": key, "num": letter_dict[key]})
    
    def myFunc(e):
        return e["num"]

    
    
    sorted_dict.sort(reverse= True, key=myFunc)

    print("")
    for i in sorted_dict:
        print(f"The '{i["letter"]}' character was found {i["num"]} times")
    print("--- End report ---")
 

  

    
    





    
    
def count_letter(text):
    lower_text = to_lower(text)
    letter_set = set()
    letter_dic = {}
    for letter in lower_text: 
        if letter.isalpha(): #agrega al set los caracteres diferentes que encuentre
            letter_set.add(letter)

    
    for letter in letter_set:   #llena el diccionario con letras e inicia su contador a cero 
        letter_dic[letter] = 0

    
    for letter in lower_text:
        if letter.isalpha():
            letter_dic[letter] += 1

    return letter_dic
    

def to_lower(text):
    lower_text = text.lower()
    return lower_text

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    
    return len(words)


main()
