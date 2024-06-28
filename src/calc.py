
def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "오류: 0으로 나눌 수 없습니다!"
    
def calculator():
    while True:
        print("\n계산기")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("q. 종료")

        choice = input("원하는 연산을 선택하세요 (1/2/3/4/5): ")

        if choice == 'q':
            print("계산기를 종료합니다.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("첫 번째 숫자: "))
            num2 = float(input("두 번째 숫자: "))

            if choice == '1':
                print("결과:", add(num1, num2))
            elif choice == '2':
                print("결과:", subtract(num1, num2))
            elif choice == '3':
                print("결과:", multiply(num1, num2))
            elif choice == '4':
                print("결과:", divide(num1, num2))
        else:
            print("input error")

if __name__ == "__main__":
    calculator()

