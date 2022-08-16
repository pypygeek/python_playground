# 캡슐화 정리
# 1. 클래스 밖에서 접근 못하게 할 변수, 메소드 정하기
# 2. 변수나 메소드 이름 앞에 언더바 2개 붙이기
# 3. 변수에 간접 접근할 수 있게 메소드 (getter / setter or 다른 용도의 메소드) 추가하기

class Person:
    """주민등록증 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """ 이름, 나이, 주민등록번호 """
        self.name = name
        self.__age = age
        self.__residgent_id = resident_id
    
    """ 객체의 속성과 그것을 사용하는 행동(메소드)를 하나로 묶어서 직접 접근으로는 설정이 불가하지만 메소드를 통해 설정이 가능"""
    def authenticate(self, id_field):
        """ 음주 가능 나이인지 확인하는 메소드 """
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """ 주민 정보를 문자열로 리턴하는 메소드 """
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    @property
    def get_age(self):
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def set_age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이눈 0보다 작을 수 없습니다. 기본 값 0으로 설정합니다.")
            self._age = 0
        else:
            self._age = value

young = Person("name", 18, "1234567")
print(young.age)

young.set_age(23)
print(young.age)