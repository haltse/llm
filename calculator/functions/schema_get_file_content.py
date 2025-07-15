from google.genai import types
schema_get_file_content = types.FunctionDeclaration(
    description="reads the contents from the relative file_path which must be within the working directory. Returns a string of the file contents or an error",
    name="get_file_content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file to read",
            ),
        },
    ),
)