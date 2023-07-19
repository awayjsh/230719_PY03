import book

def rental_book(name, rental_number_of_book):
    book.decrease_book(rental_number_of_book)
    print(f"{name}님이 {rental_number_of_book}권의 책을 대여하였습니다.")

rental_book('홍길동', 3)
