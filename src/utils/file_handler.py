import pandas as pd
import PyPDF2


def extract_content(file_obj, file_name: str):
    """
    Args:
        file_obj: File object or file path
        file_name: Name of the file for display purposes
    
    Returns:
        title_string: Extracted title from the first rows (as a string)
        output_path: Path to the unmerged Excel file
    """

    if file_name.endswith(".pdf"):
        if file_obj is not None:
            # Read the PDF file
            pdf_reader = PyPDF2.PdfReader(file_obj)
            # Extract the content
            content = ""
            for i, page in enumerate(pdf_reader.pages):
                content += f"#Trang {i}:\n\n {page.extract_text()}\n\n"
        return content
    elif file_name.endswith(".csv"):
        df = pd.read_csv(file_obj)
    else:
        # Read all sheets in the Excel file as a dictionary of DataFrames
        all_sheets = pd.read_excel(file_obj, sheet_name=None)

        # Optionally, concatenate all sheets into a single DataFrame
        df = pd.concat(all_sheets.values(), ignore_index=True)
    
    # Convert DataFrame to a list of lists (first row is header, subsequent rows are data)
    headers = df.columns.tolist()
    data = df.values.tolist()
    
    # Combine headers and data
    result = [headers] + data
    
    # Convert all values to strings to ensure compatibility
    result = [[str(cell) for cell in row] for row in result]
    
    return result