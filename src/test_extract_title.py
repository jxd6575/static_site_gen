import unittest
from extract_title import extract_title, generate_page

class TestExtractTitle(unittest.TestCase):
    
    def test_extract_title(self):
        test_case = """
# Hello   

BEEP BOOP **vlosd**

### lets gooo

### more stuff
        """
        self.assertEqual("Hello", extract_title(test_case))
    
    #def test_generate_page(self):
       # generate_page("./content/index.md", "./template.html","./public/index.md")