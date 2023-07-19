# 실습 번호.py
import book

number_of_people = 0
user_info = {}
ans_list = []
name_age_address = []

def increase_user():
    global number_of_people
    number_of_people = number_of_people + 1
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(a):
    global user_info
    global ans_list
    increase_user()
    keys = ['name', 'age', 'address']
    values = [a[0],a[1],a[2]]
    user_info = dict(zip(keys,values))
    print(f"{a[0]}님 환영합니다!")
    return user_info

for i in range (len(name)) :

    name_age_address.append([name[i],age[i],address[i]])

many_user= list(map(create_user,name_age_address))

def rental_book(info):
    rental_number_of_book = int(info['age'] / 10)
    book.decrease_book(rental_number_of_book)
    print(f"{info['name']}님이 {rental_number_of_book}권의 책을 대여하였습니다.")

result = list(map(rental_book, map(lambda x : {'name' : x['name'],'age' : x['age']}, many_user)))
