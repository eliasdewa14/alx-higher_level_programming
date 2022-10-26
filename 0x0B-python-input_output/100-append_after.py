"""Define a function to inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    insert_text = ""
    with open(filename) as f:
        for line in f:
            insert_text += line
            if search_string in line:
                insert_text += new_string
    with open(filename, 'w') as f:
        f.write(insert_text)
