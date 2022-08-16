class User:
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다.")
    
    # return 값으로 print가 출력
    def __str__(self):
        return f"사용자 : {self.name}, 이메일 : {self.email}"

user1 = User("김선생", "kim@kim", "1234")

print(user1)