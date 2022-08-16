class User:
    # 인사 메세지 출력 메소드
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name} 입니다!")

    def login(self, my_email, my_password):
        if(self.email == my_email and self.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

    def check_name(self, name):
        return self.name == name

# 인스턴스
user1 = User()
user2 = User()
user3 = User()

# 속성 추가
user1.name = "파이썬"
user1.email = "python@pthon.python"
user1.password = "python"

user2.name ="C"
user2.email = "C@C.C"
user2.password = "C"

user3.name = "JAVA"
user3.email = "JAVA"
user3.password = "JAVA"

# 인스턴스 사용
print(user1.email)
print(user2.password)
print(user3.name)

# 클래스 메소드 호출
User.say_hello(user1)

# 인스턴스에 메소드 호출
user2.say_hello()

# 자동으로 1번째 파라미터 전달됨.
user3.login("JAVA", "JAVA")

print(user1.check_name("GO"))
