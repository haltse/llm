from google.genai import types
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to file_path constrained to the working directory. Returns success message with file_path and characters written or an error message",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path (within the working directory) to write the content to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ))
