from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil
from pathlib import Path

def extract_title(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    #print(markdown_blocks)
    for block in markdown_blocks:
        if block_to_block_type(block) == BlockType.HEADING and block.startswith("# "):
            return block.strip("# ")

    raise Exception("No h1 '#' header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    from_file_read = from_file.read()
    from_file.close()


    template_file = open(template_path)
    template_file_read = template_file.read()
    template_file.close()

    from_file_HTMLNode = markdown_to_html_node(from_file_read)
    #print(from_file_HTMLNode)
    from_file_HTML_string = from_file_HTMLNode.to_html()
    title = extract_title(from_file_read)
    replaced_template = template_file_read.replace("{{ Title }}", title).replace("{{ Content }}", from_file_HTML_string)
    replaced_template = replaced_template.replace('href="/', f'href="{basepath}').replace('src="/',f'src="{basepath}')
    # Create directory structure if it doesn't exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:  # Only try to create if there's a directory part
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(replaced_template)
    #print(from_file.closed)
    #print(template_file.closed)
    #print(template_file_read)
    #print(from_file_read)
    #print(replaced_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    #print(os.listdir(dir_path_content))
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)