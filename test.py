from src.htmlnode import HTMLNode

node = HTMLNode(
    "p",
    "Paragraph text",
    ["child1", "child2"],
    {"href": "https://123.com", "href2": "https://456.com"},
)


for prop in node.props:
    print(prop, node.props[prop])
