import logging
import azure.functions as func


def main(req: func.HttpRequest, Biblioteca: func.Out[str]) -> func.HttpResponse:
    #book = open("file.txt", "w", encoding="utf-8")
    #book.write("Hello, It's me AGAIN")
    #book.close()
    Biblioteca.set("Hello, It's me")
    return func.HttpResponse("Function executed!!!")        