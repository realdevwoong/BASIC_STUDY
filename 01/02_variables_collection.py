# ==========================================
# 02_variable_collection.py
# 2강: 변수와 컬렉션 자료형 + 메소드 예제
# ==========================================

# 여러 사용자 정보를 리스트, 튜플, 딕셔너리, 세트로 저장
user_ids_list = [1001, 1002, 1003]
user_emails_tuple = ("a@example.com", "b@example.com", "c@example.com")
user_passwords_dict = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}
user_roles_set = {"admin", "editor", "viewer"}

# 값 + 자료형 + 메모리 주소 출력
print("[컬렉션 자료형 확인]")
print("user_ids_list:", user_ids_list, "| type:", type(user_ids_list), "| id:", id(user_ids_list))
print("user_emails_tuple:", user_emails_tuple, "| type:", type(user_emails_tuple), "| id:", id(user_emails_tuple))
print("user_passwords_dict:", user_passwords_dict, "| type:", type(user_passwords_dict), "| id:", id(user_passwords_dict))
print("user_roles_set:", user_roles_set, "| type:", type(user_roles_set), "| id:", id(user_roles_set))

# ------------------------------------------
# 컬렉션 메소드 예제
# ------------------------------------------

print("\n[리스트 메소드 예제]")
user_ids_list.append(1004)       # 추가
print("user_ids_list after append & remove:", user_ids_list)

user_ids_list.remove(1002)       # 삭제
print("user_ids_list after append & remove:", user_ids_list)

print("\n[튜플 특징 예제]")
# 튜플은 불변(immutable), 직접 변경 불가
print("user_emails_tuple[0]:", user_emails_tuple[0])
# user_emails_tuple[0] = "new@example.com"  # 실행하면 오류 발생
# 1. 튜플 → 리스트 변환
temp_list = list(user_emails_tuple)

# 2. 리스트에서 수정
temp_list[0] = "new@example.com"

# 3. 다시 튜플로 변환
user_emails_tuple = tuple(temp_list)

print(user_emails_tuple)
# 출력: ('new@example.com', 'b@example.com', 'c@example.com')


print("\n[딕셔너리 메소드 예제]")
user_passwords_dict["user4"] = "pass4"  # 새 키-값 추가
del user_passwords_dict["user2"]        # 키-값 삭제
print("user_passwords_dict after add & delete:", user_passwords_dict)

print("\n[세트 메소드 예제]")
user_roles_set.add("guest")      # 추가
print("user_roles_set after add & remove:", user_roles_set)

user_roles_set.remove("editor")  # 삭제
print("user_roles_set after add & remove:", user_roles_set)
