L = input("Nhập vào danh sách các chuỗi và số nguyên, cách nhau bởi dấu phẩy: ").split(',')
strings = [x for x in L if isinstance(x, str)]
integers = [int(x) for x in L if x.isdigit()]

max_length_string = max(strings, key=len) if strings else None
min_value_integer = min(integers) if integers else None

print("Chuỗi có độ dài lớn nhất: ", max_length_string)
print("Số nguyên có giá trị nhỏ nhất: ", min_value_integer)

