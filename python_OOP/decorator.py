# 데코레이터 : 기존의 함수에 새로운 기능 추가!
def print_hello():
    print('안녕하세요!')

# 파라미터를 함수로 받고 함수를 꾸며줌
def add_pint_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

# return된 함수를 호출하기 위해서 뒤에 ()로 호출ㅊ
add_pint_to(print_hello)()

# 위와 같은 코드 직관적으로
print_hello = add_pint_to(print_hello)
print_hello()

# 데코레이터 이용해서 다른 함수 꾸미기
@add_pint_to
def print_bye():
    print("안녕히가세용")