import xml.etree.ElementTree as etree

def check_depth(root):
    children = []
    for i in root:
        children.append(i)
    
    if len(children) == 0:
        return 0
    
    return 1 + max( check_depth(child) for child in children )

def depth(elem, level):
    global maxdepth
    maxdepth = check_depth(elem)
    
maxdepth = 0
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)