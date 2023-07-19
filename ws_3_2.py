number_of_people = 0
user_info = {}

def increase_user():
    global number_of_people
    number_of_people = number_of_people + 1
    pass

def create_user(name,age,address):
    global user_info
    increase_user()
    keys = ['name', 'age', 'address']
    values = [name, age, address]
    user_info = dict(zip(keys,values))
    print(f"{name}님 환영합니다!")
    # print(user_info)
    return user_info

def now_people() :
    print(f"현재 가입 된 유저 수 : {number_of_people}")

now_people()
print(create_user('홍길동',30,'서울'))
now_people()