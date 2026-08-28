from markdown_to_blocks import block_to_block_type, markdown_to_blocks
from textnode import text_node_to_html_node
from htmlnode import HTMLNODE, LeafNode , ParentNode
markdown = md = """
This is **bolded** paragraph
text in a p
tag here

### This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
def markdown_to_html_node(markdown):
    split_mark = markdown_to_blocks(markdown)
    block_type_list = []
    for block in split_mark:
        block_type_list.append(block_to_block_type(block))
    
    print(block_type_list)
markdown_to_html_node(markdown)
