from textnode import TextNode
from textnode import TextType
from htmlnode import props_to_html
def main():
    node = TextNode("this is an anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    print(props_to_html.result)
main()


