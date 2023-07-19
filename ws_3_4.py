number_of_people = 0
user_info = {}
ans_list = []
name_age_address = []

def increase_user():
    global number_of_people
    number_of_people = number_of_people + 1
    pass

def create_user(a):
    global user_info
    global ans_list
    increase_user()
    keys = ['name', 'age', 'address']
    values = [a[0],a[1],a[2]]
    user_info = dict(zip(keys,values))
    print(f"{a[0]}님 환영합니다!")
    return user_info

def now_people() :
    print(f"현재 가입 된 유저 수 : {number_of_people}")


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in range (len(name)) :

    name_age_address.append([name[i],age[i],address[i]])

ans_list = list(map(create_user,name_age_address))

print(ans_list)