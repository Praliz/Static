from split_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType
from split_delimiter import split_nodes_delimiter , split_nodes_image , split_nodes_link


def text_to_textnodes(text):
    step1 = split_nodes_delimiter([TextNode(text,TextType.TEXT)],"_",TextType.ITALIC)
    step2 = split_nodes_delimiter(step1,"**",TextType.BOLD)
    step3 = split_nodes_delimiter(step2,"`",TextType.CODE)
    step4 = split_nodes_image(step3)
    step5 = split_nodes_link(step4)
    return step5
  