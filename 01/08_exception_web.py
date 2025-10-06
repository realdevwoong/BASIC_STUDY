# ==========================================
# 08_exception_web.py
# 8강: 예외 처리 (try / except / finally / raise)
# ==========================================

# 1) 사용자 입력 예외 처리 - 포인트 입력
try:
    user_points = int(input("포인트를 입력하세요: "))
except ValueError:
    print("잘못된 입력입니다. 숫자만 입력하세요.")
    user_points = 0
finally:
    print(f"입력된 포인트: {user_points}")

# 2) 주문 총액 계산에서 예외 처리
def calculate_total(price, quantity, delivery_fee=3000):
    if price < 0 or quantity < 0:
        raise ValueError("가격과 수량은 0 이상이어야 합니다.")
    return price * quantity + delivery_fee

try:
    order_price = int(input("상품 가격을 입력하세요: "))
    order_quantity = int(input("수량을 입력하세요: "))
    total = calculate_total(order_price, order_quantity)
    print(f"총액: {total:,}원")
except ValueError as e:
    print(f"주문 처리 오류: {e}")

# 3) 쿠폰 적용 예외 처리
def apply_coupon(total_amount, coupon_code):
    coupons = {"WELCOME10": 0.1, "HOLIDAY5": 0.05, "VIP20": 0.2}
    if coupon_code.upper() not in coupons and coupon_code.upper() != "N":
        raise ValueError(f"유효하지 않은 쿠폰 코드: {coupon_code}")
    discount = coupons.get(coupon_code.upper(), 0)
    return int(total_amount * (1 - discount))

coupon_input = input("쿠폰 코드를 입력하세요 (없으면 N): ")
try:
    final_total = apply_coupon(total, coupon_input)
    print(f"쿠폰 적용 후 총액: {final_total:,}원")
except ValueError as e:
    print(e)
    
# 1) 포인트 입력
# 정상 입력
# 입력: 750
# 출력: 입력된 포인트: 750

# 잘못된 입력
# 입력: abc
# 출력: 잘못된 입력입니다. 숫자만 입력하세요.
#       입력된 포인트: 0

# 2) 상품 가격 / 수량 입력
# 정상 입력
# 입력: 가격 18000, 수량 2
# 출력: 총액: 39000원

# 잘못된 입력
# 입력: 가격 -1000, 수량 2
# 출력: 주문 처리 오류: 가격과 수량은 0 이상이어야 합니다.

# 3) 쿠폰 입력
# 유효 쿠폰
# 입력: WELCOME10 / HOLIDAY5 / VIP20
# 출력: 쿠폰 적용 후 총액: XXX원

# 쿠폰 미사용
# 입력: N
# 출력: 쿠폰을 사용하지 않아 총액은 XXX원 입니다.

# 잘못된 쿠폰
# 입력: SAVE50
# 출력: 유효하지 않은 쿠폰 코드: SAVE50