from textnode import TextNode
from textnode import TextType
from extract_markdown_images import extract_markdown_images
from extract_markdown_images import extract_markdown_links
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        count_delimiter = node.text.count(delimiter)
        if not count_delimiter % 2 == 0:
            raise Exception("invalid Markdown")

        parts = node.text.split(delimiter)
        for index, part in enumerate(parts):
            if part =="":
                continue
            if index % 2 ==0:
                new_list.append(TextNode(part,TextType.TEXT))
            else:
                new_list.append(TextNode(part,text_type))
    return new_list
        
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        extracted_node = extract_markdown_images(node.text)
        if extracted_node == []:
            new_list.append(node)
            continue
        else:
            remaining_text = node.text
            for img,url in extracted_node:
                section = remaining_text.split(f"![{img}]({url})",1)
                if section[0] != "":
                    new_list.append(TextNode(section[0],TextType.TEXT))
                new_list.append(TextNode(img,TextType.IMAGE,url))
                remaining_text = section[1]
            if remaining_text != "":
                new_list.append(TextNode(remaining_text,TextType.TEXT))
    return new_list       
        
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        extracted_node = extract_markdown_links(node.text)
        if extracted_node == []:
            new_list.append(node)
            continue
        else:
            remaining_text = node.text
            for link,url in extracted_node:
                section = remaining_text.split(f"[{link}]({url})",1)
                if section[0] != "":
                    new_list.append(TextNode(section[0],TextType.TEXT))
                new_list.append(TextNode(link,TextType.LINK,url))
                remaining_text = section[1]
            if remaining_text != "":
                new_list.append(TextNode(remaining_text,TextType.TEXT))
    return new_list       