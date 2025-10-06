# ==========================================
# 05_conditional_web.py
# 5강: 조건문 (If / Elif / Else) - 웹 개발 실전 예제
# ==========================================

# 사용자 입력 받기
user_name = input("이름을 입력하세요: ")
user_points = int(input("포인트를 입력하세요: "))
user_role = input("권한(admin/editor/viewer)을 입력하세요: ")
coupon_code = input("쿠폰 코드를 입력하세요 (없으면 N): ")

print("\n[조건문 실습]")

# 1) 포인트 기준 회원 등급
if user_points >= 1000:
    print(f"{user_name}님은 VIP 회원입니다.")
elif 500 <= user_points < 1000:
    print(f"{user_name}님은 골드 회원입니다.")
elif 100 <= user_points < 500:
    print(f"{user_name}님은 일반 회원입니다.")
else:
    print(f"{user_name}님은 신규 회원입니다.")

# 2) 사용자 권한 확인
if user_role == "admin":
    print(f"{user_name}님은 관리자 권한이 있습니다.")
elif user_role == "editor":
    print(f"{user_name}님은 편집자 권한이 있습니다.")
elif user_role == "viewer":
    print(f"{user_name}님은 일반 사용자입니다.")
else:
    print(f"{user_name}님은 알 수 없는 권한입니다.")

# 3) 쿠폰 적용 여부 확인
valid_coupons = ["WELCOME10", "HOLIDAY5", "VIP20"]
if coupon_code.upper() in valid_coupons:
    print(f"{user_name}님, 쿠폰 {coupon_code.upper()}이 적용되었습니다!")
elif coupon_code.upper() == "N":
    print(f"{user_name}님은 쿠폰을 사용하지 않았습니다.")
else:
    print(f"{user_name}님, 입력한 쿠폰 {coupon_code}은 유효하지 않습니다.")
