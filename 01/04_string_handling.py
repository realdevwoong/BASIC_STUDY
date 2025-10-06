# ==========================================
# 02_input_string.py
# 2강~2.5강: 문자열 처리 + 사용자 입력 + 출력 포맷팅
# ==========================================

# 1) 사용자 입력 받기
user_name = input("이름을 입력하세요: ")
user_email = input("이메일을 입력하세요: ")
user_age = int(input("나이를 입력하세요: "))

# 2) 기본 출력
print("\n[기본 출력]")
print("사용자 이름:", user_name)
print("사용자 이메일:", user_email)
print("사용자 나이:", user_age)

# 3) 문자열 메소드 활용
print("\n[문자열 메소드]")
print("이름 대문자:", user_name.upper())
print("이메일 소문자:", user_email.lower())
print("이메일 도메인:", user_email.split("@")[1])

# 4) f-string 포맷팅
print("\n[f-string 포맷팅]")
print(f"{user_name}님의 이메일은 {user_email}이고, 나이는 {user_age}살 입니다.")

# 5) format() 메소드 포맷팅
print("\n[format() 포맷팅]")
print("{}님의 이메일은 {}이고, 나이는 {}살입니다.".format(user_name, user_email, user_age))

# 6) % 포맷팅
print("\n[% 포맷팅]")
print("%s님의 이메일은 %s이고, 나이는 %d살입니다." % (user_name, user_email, user_age))
