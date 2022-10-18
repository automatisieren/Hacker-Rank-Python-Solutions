import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    result = 0
    for i in node.iter():
        ln = len(i.attrib)
        if ln != 0:
            result += len(i.attrib)
    return result

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))