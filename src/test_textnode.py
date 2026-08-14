import unittest
from textnode import TextNode, TextType


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
        
   
        
        


if __name__ == "__main__":
    unittest.main()