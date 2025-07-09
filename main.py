import os
import sys
from google import genai 
from dotenv import load_dotenv
from google.genai import types
import sys
 # Assuming the first command-line argument is always the working directory
from config import MAX_CHARS 
 
from functions.schema_get_files_info import schema_get_files_info
from functions.schema_get_file_content import schema_get_file_content
from functions.schema_run_python import schema_run_python_file
from functions.schema_write_file import schema_write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from  functions.write_file import write_file
from  functions.run_python_file import run_python_file
available_functions = types.Tool(
    function_declarations=[schema_run_python_file,schema_get_files_info,schema_write_file,schema_get_file_content]
)

try:
    print(f"DEBUG sys.argv: {sys.argv}, length: {len(sys.argv)}")
    if len(sys.argv) >= 3:
        working_directory = sys.argv[1]
        user_prompt = sys.argv[2]
    elif len(sys.argv) == 2:
        working_directory = "."
        user_prompt = sys.argv[1]
    else:
        print("Usage: python main.py <working_directory> <prompt>")
        exit(1)
    

    system_prompt = """
    You are a helpful AI coding agent. 

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
   
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=genai.types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )





    usage_metadata = response.usage_metadata



    if response.function_calls:
        
        
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
             
            function_map = {
            "get_file_content": get_file_content,
            "write_file": write_file,
            "run_python_file": run_python_file,
            "get_files_info": get_files_info,

        
    }
        for function_call in response.function_calls:
            
            func = function_map.get(function_call.name)
            if func:
                args = dict(function_call.args)  # Make a mutable copy
                if 'working_directory' in args:
                    del args['working_directory']
                result = func(working_directory=working_directory, **args)
                #result = func(working_directory=working_directory, **function_call.args)
                print(result)
            else:
                print(f"Unknown function: {function_call.name}")

    else:
        print(response.text)

    if len(sys.argv) <= 2:
        pass
    else:
        if sys.argv[2] =='--verbose':
            print(f'User prompt: {sys.argv[1]}\nPrompt tokens: {usage_metadata.prompt_token_count}\nResponse tokens: {usage_metadata.candidates_token_count}')
    
    
    

except Exception as e:
    print(f"Error: {e}")
    import sys
    sys.exit(1)