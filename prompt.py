from . import chroma_collection

class Prompt:
    system_template = {
        "role": "system",
        "content": "You are an AI assistant that helps developer write c# code."
        "You will be given a sample code and some instructions with code examples."
        "You need to generate desired code based on the sample."
        "You should always follow the instructions when generating the code."
    }
    
    def __init__(self, query: str = "") -> None:
        """
        Args:
            query (str): query to use as prompt
        """
        super().__init__()
        self.query = query
    
    def get_prompt(self, code: str, is_first_prompt: bool = True) -> list[dict[str, str]]:
        """Generate the prompts for the given code

        Args:
            code (str): input code
            is_first_prompt (bool, optional): If thie is the first prompt. We need to append system prompt and code if it is,
            otherwise we only need base prompt. Defaults to True.

        Returns:
            list[dict[str, str]]: prompts
        """
        if is_first_prompt:
            base_template = {
                "role": "user",
                "content": f"""Here is the sample code:\n```csharp\n{code}\n{self.get_user_content()}```"""
            }
            return [Prompt.system_template, base_template]

        base_template = {
            "role": "user",
            "content": self.get_user_content()
        }
        return [base_template]
    
    def get_context(self) -> str:
        """Get the context for the given query from chromadb
        Returns:
            str: context
        """
        results = chroma_collection.query(
            query_texts=[self.query],
            n_results=1,
            include = ["documents"]
        )
        return results['documents'][0]
    
    def get_user_content(self):
        return f'{self.query}\nHere is the instruction:\n{self.get_context()}'
