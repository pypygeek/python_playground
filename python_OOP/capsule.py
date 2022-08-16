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

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

young = Person("name", 18, "1234567")
print(young.get_age())

young.set_age(23)
print(young.get_age())