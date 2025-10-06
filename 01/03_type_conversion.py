# ==========================================
# 03_type_conversion.py
# 3강: 자료형 변환 (기본 + 컬렉션)
# ==========================================

# 기본 자료형 변환
num_int = 10
num_float = float(num_int)   # int → float
num_str = str(num_int)       # int → str

print("[기본 자료형 변환]")
print("num_int:", num_int, "| type:", type(num_int), "| id:", id(num_int))
print("num_float:", num_float, "| type:", type(num_float), "| id:", id(num_float))
print("num_str:", num_str, "| type:", type(num_str), "| id:", id(num_str))

# 컬렉션 자료형 변환
list_data = [1, 2, 3]
tuple_data = tuple(list_data)  # list → tuple
set_data = set(list_data)      # list → set

print("\n[컬렉션 자료형 변환]")
print("list_data:", list_data, "| type:", type(list_data), "| id:", id(list_data))
print("tuple_data:", tuple_data, "| type:", type(tuple_data), "| id:", id(tuple_data))
print("set_data:", set_data, "| type:", type(set_data), "| id:", id(set_data))