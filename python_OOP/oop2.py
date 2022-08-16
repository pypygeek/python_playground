# 클래스 변수 연습
class User:
    count = 0
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        # 인스턴스를 생성할 때마다 1씩 증가
        User.count += 1

user1 = User("test", "test@test.com", "1234")
user2 = User("test2", "test2@test.com", "1234")

print(User.count)

# 클래스 변수(한 클래스의 모든 인스턴스가 공유하는 속성) 설정
User.count = 5

print(User.count)
print(user1.count)

# 인스턴스 변수 설정
user2.count = 2
print(user2.count)