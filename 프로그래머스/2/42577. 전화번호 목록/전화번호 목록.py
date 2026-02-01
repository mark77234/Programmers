
def solution(phone_book):

    books = sorted(phone_book)

    for i in range(len(books) - 1):
        if books[i] == books[i + 1][: len(books[i])]:
            return False

    return True