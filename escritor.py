special_simbols = [' ', 'ˈ', 'ˌ', 'ː']
vowels = ['ɑ', 'æ', 'e', 'ɛ', 'i', 'ɪ', 'ə', 'ɚ', 'ɝ', 'ʌ', 'ɔ', 'ɒ', 'u', 'ʊ']
consonants = ['b', 'd', 'f', 'ɡ', 'h', 'k', 'l', 'm', 'n', 'p', 's', 't', 'v', 'w', 'z', 'r', 't̮', 'ʃ', 'ʒ', 'θ', 'ð', 'ŋ', 'y', 'j']
simbols = special_simbols + vowels + consonants

def make_books():
    book = open("book 1", "w", encoding="utf-8")
    for simbol in simbols:
        book.write(f" {simbol} ")
    
    book.close()

if __name__ == "__main__":
    make_books()