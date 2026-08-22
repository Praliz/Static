from textnode import TextNode
from textnode import TextType
import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    result = re.findall(pattern, text)
    return result

def extract_markdown_links(text):
    pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    result = re.findall(pattern,text)
    return result