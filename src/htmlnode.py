

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #Str rep of HTML tag p, a ,h1
        self.value = value # value of html tag
        self.children = children #A list of htmlnode obj
        self.props = props # dict of key-val repping attr of html tag

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_in_html = ""
        if self.props is None:
            return ""
        if self.props:
            tup_of_props = self.props.items()
            for tup in tup_of_props:
                key, value = tup
                props_in_html += f' {key}="{value}"'
        return props_in_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" #{self.props_to_html()} add if you want to see func as well

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        #print(self.value)
        if not self.value:
            raise ValueError("All leafnodes must have a value")
        
        if not self.tag:
            return self.value
        #if not self.props:
        #    return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Must have a tag")
        if not self.children:
            raise ValueError("Must have children")
        child_to_html = ""
        for child in self.children:
            child_to_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_to_html}</{self.tag}>"
    
     def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"