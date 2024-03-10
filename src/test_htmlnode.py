import unittest

from htmlnode import HTMLNode


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

    def test_repr(self):
        pass
