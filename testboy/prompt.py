from chromadb import Collection

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
    
    def get_prompt(self, 
                   code: str, 
                   collection: Collection, 
                   is_first_prompt: bool = True,
                   n_results: int = 1
        ) -> list[dict[str, str]]:
        """Generate the prompts for the given code

        Args:
            code (str): input code
            collection (Collection): chromadb collection
            is_first_prompt (bool, optional): If thie is the first prompt. We need to append system prompt and code if it is, otherwise we only need base prompt. Defaults to True.
            n_results (int, optional): number of results to return from chromadb. Defaults to 1.

        Returns:
            list[dict[str, str]]: prompts
        """
        if is_first_prompt:
            base_template = {
                "role": "user",
                "content": f"""Here is the sample code:\n```csharp\n{code}\n{self.merge_contexts(collection, n_results)}```"""
            }
            return [Prompt.system_template, base_template]

        base_template = {
            "role": "user",
            "content": self.merge_contexts(collection, n_results)
        }
        return [base_template]
    
    def merge_contexts(self, collection: Collection, n_results: int) -> str:
        """Get the context for the given query from chromadb, merge the contexs with the query
        Args:
            collection (Collection): chromadb collection
        Returns:
            str: context
        """
        results = collection.query(
            query_texts=[self.query],
            n_results=n_results,
            include = ["documents"]
        )
        contexts: str = "\n".join(results['documents'][0])
        return f"{self.query}\nHere are the instructions:\n{contexts}"
