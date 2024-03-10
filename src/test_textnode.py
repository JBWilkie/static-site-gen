import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Test text", text_type_bold, "123.com")
        node2 = TextNode("Test text", text_type_bold, "123.com")
        self.assertEqual(node1, node2)

    def test_eq_false(self):
        node1 = TextNode("Test text", text_type_bold, "123.com")
        node2 = TextNode("Test texT", text_type_bold, "123.com")
        self.assertNotEqual(node1, node2)

    def test_eq_false_2(self):
        node1 = TextNode("Test text", text_type_italic, "123.com")
        node2 = TextNode("Test text", text_type_italic)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Test text", text_type_bold, "123.com")
        self.assertEqual("TextNode(Test text, bold, 123.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
