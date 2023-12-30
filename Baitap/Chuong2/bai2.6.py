import json

# Chuỗi JSON
json_data = '{"name": "Giang", "age": 19, "city": "Nam Dinh"}'

# Chuyển đổi JSON thành đối tượng Python
python_object = json.loads(json_data)

# In đối tượng Python
print("Đối tượng Python:")
print(python_object)
