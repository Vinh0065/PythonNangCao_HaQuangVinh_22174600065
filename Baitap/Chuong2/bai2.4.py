import xml.dom.minidom

doc = xml.dom.minidom.parse('sample.xml')

all_elements = doc.getElementsByTagName('*')

for element in all_elements:
    print(f"Tên phần tử: {element.tagName}")
