#변수와 자료형(Variable & Data Type)

# 사용자 입력 데이터 저장
user_name = "techinwoong"  # 문자열
user_age = 20        # 정수
user_height = 180.5  # 실수
is_member = True     # 불리언

# 변수 값 출력 + 자료형 확인 + 메모리 주소
print("이름:", user_name, "| 자료형:", type(user_name), "| id:", id(user_name))
print("나이:", user_age, "| 자료형:", type(user_age), "| id:", id(user_age))
print("키:", user_height, "| 자료형:", type(user_height), "| id:", id(user_height))
print("회원 여부:", is_member, "| 자료형:", type(is_member), "| id:", id(is_member))

# -------------------------------
# 두 번째 변수 세트 (같은 값)
# -------------------------------
user_name2 = "techinwoong"  # 문자열
user_age2 = 20               # 정수
user_height2 = 180.5         # 실수
is_member2 = True            # 불리언

# 변수 값 출력 + 자료형 확인 + 메모리 주소
print("이름2:", user_name2, "| 자료형:", type(user_name2), "| id:", id(user_name2))
print("나이2:", user_age2, "| 자료형:", type(user_age2), "| id:", id(user_age2))
print("키2:", user_height2, "| 자료형:", type(user_height2), "| id:", id(user_height2))
print("회원 여부2:", is_member2, "| 자료형:", type(is_member2), "| id:", id(is_member2))

# ✅ 자료형 변환
age_str = str(user_age)       # int -> str
height_int = int(user_height) # float -> int
is_member_str = str(is_member) # bool -> str

print("변환 후 나이:", age_str, type(age_str))
print("변환 후 키:", height_int, type(height_int))
print("변환 후 회원 여부:", is_member_str, type(is_member_str))

# ✅ 여러 변수 동시에 선언
x, y, z = 10, 20, 30
print("여러 변수:", x, y, z)

# ✅ 변수 값 교환
x, y, z = z, x, y
print("교환 후 값:", x, y, z)

