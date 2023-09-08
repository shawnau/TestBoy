import os
import openai
from prompts import Prompt
from io_utils import load_file, dump_file, extract_code


class Context:
    openai.api_key = os.getenv("OPENAI_KEY")
    openai.api_base = os.getenv("OPENAI_ENDPOINT")
    
    def __init__(self, 
                 code_paths: list[str], 
                 class_name: str = None, 
                 model_name: str = 'gpt-4', 
                 refresh_session: bool = False,
                 debug: bool = False):
        """init context based on code paths

        Args:
            code_paths (list[str]): code need to feed into the context, the first file will be used to generate test, others can be passed in as dependency.
            class_name (str, optional): We use filename as class name by defult. This should be set in case class name is different from the file name.
            model_name (str, optional): model name. Defaults to 'gpt-4'.
            refresh_session (bool, optional): clean session before each prompt chaining. Defaults to False. Use this only if your session is exceeding maxmium token limit.
            debug (bool, optional): debugging mode to print out prompt. Defaults to False.
        """
        self.model_name = model_name
        self.debug = debug
        self.refresh_session = refresh_session
        self.prompts = []
        
        self.input = '\n'.join([load_file(code_path) for code_path in code_paths])
        self.file_name = os.path.basename(code_paths[0])
        self.class_name = class_name if class_name != None else os.path.basename(code_paths[0]).split('.')[0]
    
    
    def invoke_api(self, prompt: list[dict[str, str]]) -> str:
        """Invoke openai api to generate response containing test code

        Args:
            prompt (list[dict[str, str]]): input prompt

        Returns:
            str: response content containing test code
        """
        return openai.ChatCompletion.create(
            model=self.model_name,
            messages = prompt,
            temperature=0.7,
            max_tokens=4096,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
    
    def dump(self, output_path: str):
        """dump file to destination

        Args:
            output_path (str): dump file path
        """
        dump_file(output_path, self.input)
    
    def prompt_chaining(self, prompts: list[Prompt]):
        """
        1. call gpt to get response for each prompt
        2. pass last response to next prompt
        3. repeat 1 and 2 until all prompts are processed
        """
        
        for i, prompt in enumerate(prompts):
            print(f"calling prompt {i}...")
            user_prompt = prompt(self.input, len(self.prompts) == 0)
            self.prompts += user_prompt
            response = self.invoke_api(self.prompts)
            response_msg = response.choices[0].message
            assistant_prompt = [{'role': response_msg.role, 'content': response_msg.content}]
            self.prompts += assistant_prompt
            self.input = extract_code(response_msg.content)

            if self.refresh_session:
                self.clean_session()
            if self.debug:
                print(user_prompt)
                print(assistant_prompt)
    
    def clean_session(self):
        self.prompts = []

