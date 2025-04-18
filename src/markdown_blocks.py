def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = [block.strip() for block in blocks if block.strip()]
    return clean_blocks