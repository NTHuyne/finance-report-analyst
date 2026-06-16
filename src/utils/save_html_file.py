def save_html_to_file(html_string: str, file_name: str = "report.html"):
    """
    Use this function to Save the HTML string to a file.
    
    Args:
        html_string (str): The HTML string to save.
        file_name (str): The name of the file to save the HTML string to. Defaults to "report.html".
    
    Returns:
        str: The name of the file where the HTML string was saved.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_string)
    
    return file_name