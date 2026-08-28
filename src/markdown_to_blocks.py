from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST ="unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    if markdown.startswith(("```\n")) and markdown.endswith(("```")):
        return BlockType.CODE
    lines = markdown.split("\n")
    quote_check = True
    unorder_check = True
    for line in lines:
        if not line.startswith((">")):
            quote_check = False
            break
    if quote_check:
        return BlockType.QUOTE
    for line in lines:
        if not line.startswith("- "):
            unorder_check = False
            break
    if unorder_check:
        return BlockType.UNORDERED_LIST
    order_check = True
    num = 1
    for line in lines:
        if not line.startswith(f"{num}. "):
            order_check = False
            break
        num += 1
    if order_check:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH




def markdown_to_blocks(markdown):
    split_string = markdown.split("\n\n")
    blocks = []
    for i in split_string:
        check = i.strip()
        if check != "":
            blocks.append(check)
    return blocks
