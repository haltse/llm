import os
from config import MAX_CHARS
def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory'

    try:
        # Ensure parent directories exist
        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Now write (or overwrite) the file
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing file \"{file_path}\": {e}'