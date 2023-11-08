import re

def dump_file(file_name, code):
    with open(file_name, "w") as file:
        file.write(code)

def extract_code(code):
    pattern = r"```csharp(.*?)```"  # Regular expression to capture c# code
    matches = re.findall(pattern, code, re.DOTALL)  # Use re.DOTALL to match across newlines

    if matches:
        extracted_code = matches[0].strip()
        return extracted_code
    else:
        return ""

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code_string = file.read()
        return code_string
    except Exception as e:
        print(f"Error loading code file: {e}")
        return None