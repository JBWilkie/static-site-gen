import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "Paragraph text",
            ["child1", "child2"],
            {"href": "https://123.com", "href2": "https://456.com"},
        )
        self.assertEqual(
            node.props_to_html(), " href=https://123.com href2=https://456.com"
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "My leaf node")
        self.assertEqual(node.to_html(), "<p>My leaf node</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "My leaf node")
        self.assertEqual(node.to_html(), "My leaf node")
