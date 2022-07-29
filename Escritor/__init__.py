import logging
import random
import azure.functions as func

special_simbols = [' ', 'ˈ', 'ˌ', 'ː']
vowels = ['ɑ', 'æ', 'e', 'ɛ', 'i', 'ɪ', 'ə', 'ɚ', 'ɝ', 'ʌ', 'ɔ', 'ɒ', 'u', 'ʊ']
consonants = ['b', 'd', 'f', 'ɡ', 'h', 'k', 'l', 'm', 'n', 'p', 's', 't', 'v', 'w', 'z', 'r', 't̮', 'ʃ', 'ʒ', 'θ', 'ð', 'ŋ', 'y', 'j']
simbols = special_simbols + vowels + consonants

def make_book() -> str:
    
    limit_simbols = len(simbols)-1
    letters_number = 80
    count_letters = 1
    rows_number = 40
    count_rows = 1
    pages_number = 410
    count_pages = 1   
    book = ""
    
    while count_pages <= pages_number:
        
        while count_rows <= rows_number:
        
            while count_letters <= letters_number:
                book = book + simbols[random.randint(0,limit_simbols)]
                count_letters += 1
        
            book = book + "\n"
            count_letters = 1
            count_rows += 1
        
        book = book + "\n"
        count_rows = 1
        count_pages += 1

    return book


def main(req: func.HttpRequest, Biblioteca: func.Out[str]) -> func.HttpResponse:
    
    Biblioteca.set(make_book())
    return func.HttpResponse("Function executed!!!")        