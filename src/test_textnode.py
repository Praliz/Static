import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        checkurl = TextNode("this is an anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertIsNotNone(checkurl.url)
    def test_text_type(self):
        node = TextNode("this node is for testing text-type",TextType.TEXT)
        self.assertTrue(node.text_type)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold_text(self):
        node = TextNode("Bold text",TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
    def test_url_(self):
        checkurl = TextNode("Click Here", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(checkurl)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value, "Click Here")
        self.assertEqual(html_node.props,{"href":"https://www.boot.dev"})
    def test_invalid_type(self):
        node = TextNode("Invalid text", "Bold text")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()