import datetime
import re

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    users = []
    while True:
        user = {}

        while True:
            id = input("사용자 이름을 입력하세요.")
            if re.match('^[가-힣]{2,4}', id):
                user["username"] = id
                break
            else:
                print("2-4글자 사이의 한글로만 작성된 사용자 이름을 입력하세요.")
    
        while True:
            password = input("비밀번호를 입력하세요.")
            if ("@" in password or "!" in password or "#" in password or "$" in password) and len(password) >= 8 and password[0].isupper():
                user["password"] = password
                break
            else:
                print("특수문자 하나를 포함하고 영문 대문자로 시작하는 8글자 이상의 비밀번호를 입력하세요.")
    
        while True:
            email = input("이메일 주소를 입력하세요.")
            if re.match(r'([a-zA-Z0-9]+)@([a-z]+)|.com', email):
                user["email"] = email
                break
            else:
                print("올바른 형식의 이메일 주소를 입력하세요.")
        user["stnr_date"] = stnr_date
        users.append(user)
        other = input("다른 사용자도 등록하시겠습니다? (Y / N)")
        if other == "Y":
            continue
        else:
            break
    return users

def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding = 'UTF-8')
    for user in user_list:
        f.write(', '.join(i for i in user.values()) + '\n')
    f.close()

def run():
    user_list = create_membership()
    load_to_txt(user_list)

run()