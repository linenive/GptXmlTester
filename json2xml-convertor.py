import json
import xml.etree.ElementTree as ET
import logger

with open('outputs/generator_2024-02-24-01-04-59.txt', 'r') as file:
    content = file.read()

json_object = json.loads(content)

# 재귀적으로 XML 요소를 생성
def build_xml_element(data, tag):
    if isinstance(data, dict):
        element = ET.Element(tag)
        for key, val in data.items():
            child = build_xml_element(val, key)
            element.append(child)
        return element
    elif isinstance(data, list):
        parent = ET.Element(tag)
        for item in data:
            child = build_xml_element(item, "item")
            parent.append(child)
        return parent
    else:
        element = ET.Element(tag)
        element.text = str(data)
        return element
    
def pretty_export(element):
    # ElementTree 3.9+에서 사용 가능
    ET.indent(element, space="\t", level=0)
    tree = ET.ElementTree(element)
    tree.write(
        logger.make_logpath("json2xml-convertor", "xml"), 
        encoding='utf-8',
        xml_declaration=True)

root = build_xml_element(json_object, "root")

pretty_export(root)
