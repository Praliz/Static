import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType
from extract_markdown_images import extract_markdown_images
from extract_markdown_images import extract_markdown_links
from split_delimiter import split_nodes_image
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks

#Testing Split + extract_markdown Functions

class TestTextNode(unittest.TestCase):
    def test_markdown_split(self):
        node = TextNode("This is a 'textcheck' node", TextType.TEXT)
        split_node = split_nodes_delimiter([node],"'",TextType.BOLD)
        expected = [TextNode("This is a ",TextType.TEXT),TextNode("textcheck",TextType.BOLD),TextNode(" node",TextType.TEXT)]
        self.assertEqual(split_node,expected)
    def test_markdown_codetext(self):
        node = TextNode("This is a code test 'code_'",TextType.TEXT)
        split_node = split_nodes_delimiter([node],"'",TextType.CODE)
        expected = [TextNode("This is a code test ",TextType.TEXT),TextNode("code_",TextType.CODE)]
        self.assertEqual(split_node,expected)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_link(self):
        matches = extract_markdown_links("This is a link[alt](https://google.com/)")
        self.assertListEqual([("alt","https://google.com/")],matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        result = text_to_textnodes("A quiet library")
        expected = [
            TextNode("A quiet library", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_plain_text_and_image(self):
        test = text_to_textnodes("a text for test ![image](https://i.imgur.com/zjjcJKZ.png)")
        expected = [TextNode("a text for test ",TextType.TEXT),TextNode("image",TextType.IMAGE,"https://i.imgur.com/zjjcJKZ.png")]
        self.assertEqual(test,expected)
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
