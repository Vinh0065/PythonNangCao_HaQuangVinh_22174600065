import xml.dom.minidom

# Đọc và phân tích tệp XML
doc = xml.dom.minidom.parse('sample.xml')

# Lấy phần tử gốc (root)
company = doc.documentElement

# Lấy thông tin từ phần tử company
company_name = company.getElementsByTagName('name')[0].firstChild.data
print(f"Tên Công ty: {company_name}")

# Lấy thông tin từ các phần tử staff
staff_elements = company.getElementsByTagName('staff')
for staff_element in staff_elements:
    staff_id = staff_element.getAttribute('id')
    staff_name = staff_element.getElementsByTagName('name')[0].firstChild.data
    staff_salary = staff_element.getElementsByTagName('salary')[0].firstChild.data
    print(f"\nID Nhân viên: {staff_id}")
    print(f"Tên Nhân viên: {staff_name}")
    print(f"Lương Nhân viên: {staff_salary}")
