import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "text test", None,{
            'key': 'value',
            'key2': 'value2'
        })
        node1 = HTMLNode("p", "test", [node], {})
        #repr(self.node)
        #print(self.node.props_to_html())
        self.assertEqual(repr(node), "HTMLNode(a, text test, None, {'key': 'value', 'key2': 'value2'})")
        self.assertEqual(repr(node1), "HTMLNode(p, test, [HTMLNode(a, text test, None, {'key': 'value', 'key2': 'value2'})], {})")
    
    
    def test_props_to_html(self):
        self.node = HTMLNode()
        self.node1 = HTMLNode("a", "sexy", [self.node], {'key': 'val'})
        self.node2 = HTMLNode("a", "sexy", [self.node1], {'key': 'val', 'key2': 'val2'})
        self.assertEqual(self.node.props_to_html(), "")
        self.assertEqual(self.node1.props_to_html(), ' key="val"')
        self.assertEqual(self.node2.props_to_html(), ' key="val" key2="val2"')
        self.assertEqual(self.node2.children[0].props_to_html(), ' key="val"')
    
    
    def test_values(self):
            node = HTMLNode(
                "div",
                "I wish I could read",
            )
            self.assertEqual(
                node.tag,
                "div",
            )
            self.assertEqual(
                node.value,
                "I wish I could read",
            )
            self.assertEqual(
                node.children,
                None,
            )
            self.assertEqual(
                node.props,
                None,
            )


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">google</a>')

    def test_leaf_to_html_a2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    #def test_leaf_no_value(self):
    #    node = LeafNode("p", None, "hello")
    #   node1 = LeafNode("p","","hi")
    #    self.assertEqual(node.test_leaf_no_value(), "ValueError: All leafnodes must have a value")
    #    self.assertEqual(node1.test_leaf_no_value(), "ValueError: All leafnodes must have a value")


if __name__ == "__main__":
    unittest.main()