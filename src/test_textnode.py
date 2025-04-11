import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "womp")
        node4 = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.ITALIC_TEXT, "womp")
        node6 = TextNode("This is a text node", TextType.BOLD, "womp")
        node7 = TextNode("This is a text", TextType.BOLD, "womp")
        node8 = TextNode("This is a text node", TextType.BOLD, "womp")
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node7, node8)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
            ) 

if __name__ == "__main__":
    unittest.main()