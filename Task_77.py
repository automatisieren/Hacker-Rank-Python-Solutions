from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(f"{data}")
        else:
            print(">>> Single-line Comment")
            print(f"{data}")            
    def handle_data(self, data: str) -> None:
        if not data == "\n":
            print(f">>> Data\n{data}")
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()