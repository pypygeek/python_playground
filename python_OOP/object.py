class User:
    # 특수 메소드(__메소드 이름__() ) : 특정 상황에서 자동으로 호출되는 메소드
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 1. User 인스턴스 생성
# 2. __init__ 메소드 자동 호출
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
