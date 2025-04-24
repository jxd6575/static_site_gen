import os
import shutil
import sys
from copystatic import copy_files_recursive
from extract_title import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs = "./docs"
from_path = "./content/index.md"
template_path = "./template.html"
to_path = "./public/index.html"
dir_path_content = "./content"
basepath = '/'
def main():
    print(basepath)
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    #generate_page(from_path, template_path, to_path)
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


if __name__ == "__main__":
    main()

