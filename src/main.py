# hello world

from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode

    





def main():
    text_text = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_text)

if __name__ == "__main__":
    main()

