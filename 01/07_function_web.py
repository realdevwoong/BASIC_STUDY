# ==========================================
# 07_function_web.py
# 7강: 함수 (def / return / 매개변수) - 웹 개발 실전 예제
# ==========================================

# 1) 기본 함수 정의와 호출
def greet_user(name):
    """사용자 이름을 받아 인사 메시지 반환"""
    return f"안녕하세요, {name}님!"

user_name = input("이름을 입력하세요: ")
print(greet_user(user_name))

# 2) 매개변수와 return 활용 - 포인트 기반 회원 등급 계산
def get_user_level(points):
    """포인트에 따라 회원 등급 반환"""
    if points >= 1000:
        return "VIP"
    elif 500 <= points < 1000:
        return "골드"
    elif 100 <= points < 500:
        return "일반"
    else:
        return "신규"

user_points = int(input("포인트를 입력하세요: "))
level = get_user_level(user_points)
print(f"{user_name}님의 회원 등급은 {level}입니다.")

# 3) 함수 + 매개변수 - 주문 총액 계산
def calculate_total(price, quantity, delivery_fee=3000):
    """상품 가격, 수량, 배달비를 받아 총액 계산"""
    return price * quantity + delivery_fee

order_price = int(input("상품 가격을 입력하세요: "))
order_quantity = int(input("수량을 입력하세요: "))
total = calculate_total(order_price, order_quantity)
print(f"{user_name}님 주문 총액: {total:,}원")

# 4) 함수 + 조건문 결합 - 쿠폰 적용
def apply_coupon(total_amount, coupon_code):
    """쿠폰 코드에 따라 할인 적용"""
    coupons = {"WELCOME10": 0.1, "HOLIDAY5": 0.05, "VIP20": 0.2}
    discount = coupons.get(coupon_code.upper(), 0)
    final_amount = int(total_amount * (1 - discount))
    return final_amount

coupon_input = input("쿠폰 코드를 입력하세요 (없으면 N): ")
if coupon_input.upper() != "N":
    final_total = apply_coupon(total, coupon_input)
    print(f"{user_name}님, 쿠폰 적용 후 총액: {final_total:,}원")
else:
    print(f"{user_name}님, 쿠폰을 사용하지 않아 총액은 {total:,}원 입니다.")
