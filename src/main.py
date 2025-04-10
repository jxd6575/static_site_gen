# hello world

from textnode import *

def main():
    text_text = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_text)

if __name__ == "__main__":
    main()

