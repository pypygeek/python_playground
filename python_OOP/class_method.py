#  클래스 메소드 : 클래스 변수의 값을 읽거나 변경

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name
        self.email
        self.password

        User.count += 1
    
    def say_hello(self):
        print(f"안녕하세요 {self.name}")
    
    def __str__(self):
        return f"사용자 {self.name}, 이메일{self.email}"
    
    # 클래스 메소드의 특별한 규칙 : 첫 번째 파라미터의 이름은 꼭! cls로 작성
    # cls는 자동 전달 
    @classmethod
    def number_of_users(cls):
        print(f"총 유저 수는 {cls.count}")

user1 = User("test", "test@test.com", "1234")
user2 = User("test2", "test2@test.com", "1234")

User.number_of_users()
user1.number_of_users()