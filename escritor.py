import random

special_simbols = [' ', 'ˈ', 'ˌ', 'ː']
vowels = ['ɑ', 'æ', 'e', 'ɛ', 'i', 'ɪ', 'ə', 'ɚ', 'ɝ', 'ʌ', 'ɔ', 'ɒ', 'u', 'ʊ']
consonants = ['b', 'd', 'f', 'ɡ', 'h', 'k', 'l', 'm', 'n', 'p', 's', 't', 'v', 'w', 'z', 'r', 't̮', 'ʃ', 'ʒ', 'θ', 'ð', 'ŋ', 'y', 'j']
simbols = special_simbols + vowels + consonants

def make_books():
    limit_simbols = len(simbols)-1
    len_row = 80
    count_row = 1
    len_pages = 40
    count_pages = 1
    len_books = 410
    count_books = 1
    limit_books = 3
    book_number = 1

    while book_number <= limit_books:

        book_name = "book " + str(book_number) + ".txt"
        book = open(book_name, "w", encoding="utf-8")
        
        while count_books <= len_books:
            
            while count_pages <= len_pages:
            
                while count_row <= len_row:
                    book.write(simbols[random.randint(0,limit_simbols)])
                    count_row += 1
            
                book.write("\n")
                count_row = 1
                count_pages += 1
            
            book.write("\n")
            count_pages = 1
            count_books += 1

        book.close()
        count_books = 1
        count_pages = 1
        count_row = 1
        book_number += 1

if __name__ == "__main__":
    make_books()