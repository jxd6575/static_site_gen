

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
        if self.props:
            tup_of_props = self.props.items()
            for tup in tup_of_props:
                key, value = tup
                props_in_html += f" {key}={value}"
        return props_in_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" #{self.props_to_html()} add if you want to see func as well