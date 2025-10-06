# ==========================================
# 1강: 변수와 기본 자료형
# 웹 개발 실전형 예제
# ==========================================
# 2) 기본 자료형 예제
print("\n[기본 자료형 예제]")

num1 = 10           # int
num2 = 3.14         # float
name = "Alice"      # str
is_active = True    # bool

print("num1:", num1, "| type:", type(num1), "| id:", id(num1))
print("num2:", num2, "| type:", type(num2), "| id:", id(num2))
print("name:", name, "| type:", type(name), "| id:", id(name))
print("is_active:", is_active, "| type:", type(is_active), "| id:", id(is_active))


# ==========================================
# 1강: 변수와 기본 자료형 + 연산 예제 확장
# ==========================================

num1 = 10           # int
num2 = 3            # int (몫/나머지 확인용)

# 기본 사칙연산
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2   # 실수 나눗셈
floor_div_result = num1 // num2  # 몫
mod_result = num1 % num2   # 나머지

print("\n[사칙연산 예제]")
print("num1 + num2 =", add_result, "| type:", type(add_result))
print("num1 - num2 =", sub_result, "| type:", type(sub_result))
print("num1 * num2 =", mul_result, "| type:", type(mul_result))
print("num1 / num2 =", div_result, "| type:", type(div_result))
print("num1 // num2 =", floor_div_result, "| type:", type(floor_div_result))
print("num1 % num2 =", mod_result, "| type:", type(mod_result))

print("[실전 예제 시작]")
# 사용자 기본 정보 저장
user_id = 1001                   # 회원 고유번호
user_email = "techinwoong@example.com"  # 이메일
user_password = "techinwoong"      # 비밀번호
user_is_admin = False            # 관리자 여부

# 변수 값 + 자료형 + 메모리 주소 출력
print("[사용자 정보 확인]")
print("user_id:", user_id, "| type:", type(user_id), "| id:", id(user_id))
print("user_email:", user_email, "| type:", type(user_email), "| id:", id(user_email))
print("user_password:", user_password, "| type:", type(user_password), "| id:", id(user_password))
print("user_is_admin:", user_is_admin, "| type:", type(user_is_admin), "| id:", id(user_is_admin))


# 사용자 기본 정보 저장
user_id = 1002                   # 회원 고유번호
user_email = "techinwoong_admin@example.com"  # 이메일
user_password = "techinwoongadmin"      # 비밀번호
user_is_admin = True            # 관리자 여부

# 변수 값 + 자료형 + 메모리 주소 출력
print("[사용자 정보 확인]")
print("user_id:", user_id, "| type:", type(user_id), "| id:", id(user_id))
print("user_email:", user_email, "| type:", type(user_email), "| id:", id(user_email))
print("user_password:", user_password, "| type:", type(user_password), "| id:", id(user_password))
print("user_is_admin:", user_is_admin, "| type:", type(user_is_admin), "| id:", id(user_is_admin))