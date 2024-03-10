from src.htmlnode import HTMLNode, LeafNode

node = LeafNode(None, "My leaf node")

html = node.to_html()
print(html)
