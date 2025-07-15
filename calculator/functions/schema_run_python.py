from google.genai import types
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",  # Match your function name
    description="Executes python file at file_path constrained to the working directory. Returns formatted output with STDOUT/STDERR and exit codes.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={ 
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file to execute.",
            ),
        },
        required=["file_path"]
    )
)