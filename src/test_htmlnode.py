import unittest

from htmlnode import HTMLNode


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
        self.assertEqual(self.node1.props_to_html(), " key=val")
        self.assertEqual(self.node2.props_to_html(), " key=val key2=val2")
        self.assertEqual(self.node2.children[0].props_to_html(), " key=val")
    
    
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







if __name__ == "__main__":
    unittest.main()