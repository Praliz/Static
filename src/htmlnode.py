class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
       raise NotImplementedError()
    def props_to_html(self):
        if self.props == None or self.props is {}:
            return ""
        result = ""
        for key, value in self.props.items():
            result += (f' {key}="{value}"')
        return result
    def __repr__(self):
        print(HTMLNode)
        
class LeafNode(HTMLNode):
    def __init__(self, tag ,value,props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
            raise ValueError("value should not be none")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    def __repr__(self):
         return f'LeafNode({self.tag}, {self.value},{self.props})'
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag should not be None")
        if self.children is None:
            raise ValueError("children is required but Missing")
        open_tag = f'<{self.tag}{self.props_to_html()}>'
        children_html= ""
        for child in self.children:
            children_html += child.to_html()
        close_tag = f'</{self.tag}>'
        return open_tag + children_html + close_tag
    