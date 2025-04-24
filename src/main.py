import os
import shutil

from copystatic import copy_files_recursive
from extract_title import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
from_path = "./content/index.md"
template_path = "./template.html"
to_path = "./public/index.html"
dir_path_content = "./content"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    #generate_page(from_path, template_path, to_path)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()

