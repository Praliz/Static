import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType
from extract_markdown_images import extract_markdown_images
from extract_markdown_images import extract_markdown_links
from split_delimiter import split_nodes_image
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