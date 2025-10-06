# ==========================================
# 06_loop_korea_web.py
# 6강: 반복문 (For / While) - 한국형 웹 개발 실전 예제
# ==========================================

# 1) 배달 주문 내역
orders = [
    {"user": "홍길동", "item": "치킨", "price": 18000, "quantity": 2},
    {"user": "김철수", "item": "피자", "price": 22000, "quantity": 1},
    {"user": "이영희", "item": "떡볶이", "price": 7000, "quantity": 3},
]

# for문: 주문 총액 계산 + 배달 팁 포함
print("[주문 내역 + 배달 총액]")
for order in orders:
    delivery_fee = 3000
    total_price = order["price"] * order["quantity"] + delivery_fee
    print(f"{order['user']}님 주문: {order['item']} x{order['quantity']} + 배달비 {delivery_fee:,}원 = 총 {total_price:,}원")

# 2) while문: 쿠폰 입력 반복
print("\n[쿠폰 입력 예제]")
valid_coupons = ["KOREA5", "WELCOME3", "HOLIDAY10"]
user_input = ""

while user_input.upper() != "EXIT":
    user_input = input("쿠폰 코드를 입력하세요 (종료: EXIT): ")
    if user_input.upper() in valid_coupons:
        print(f"{user_input} 적용 완료! 할인 혜택을 받았습니다.")
    elif user_input.upper() == "EXIT":
        print("쿠폰 입력 종료")
    else:
        print("유효하지 않은 쿠폰입니다. 다시 입력해주세요.")

# 3) 리스트 + 조건문: 고액 주문 고객 알림
print("\n[고액 주문 고객 알림]")
for order in orders:
    total_price = order["price"] * order["quantity"] + 3000
    if total_price >= 40000:
        print(f"알림: {order['user']}님은 고액 주문 고객입니다! (총 {total_price:,}원)")
