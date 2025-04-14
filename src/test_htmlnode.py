import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == "__main__":
    unittest.main()