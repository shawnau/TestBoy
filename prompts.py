

from abc import ABC, abstractmethod
from io_utils import load_file
from templates import moq_sample, nsubstitute_sample, sample_comment


class Prompt(ABC):
    system_prompt : str = "You are an AI assistant that helps developer write c# unit tests. You will genetate unit tests using MSTest framework from the given sample."

    def get_code_prompt(code: str) -> str:
        return f"""
Here is the given code: 
```csharp
{code}
```
"""
    
    def __call__(self, code: str, is_first_prompt: bool = True) -> list[dict[str, str]]:
        """Generate the prompts for the given code

        Args:
            code (str): input code
            is_first_prompt (bool, optional): If thie is the first prompt. We need to append system prompt and code if it is, otherwise we only need base prompt. Defaults to True.

        Returns:
            list[dict[str, str]]: prompts
        """
        system_template = {
            "role": "system",
            "content": Prompt.system_prompt
        }
        
        base_template = {
            "role": "user",
            "content": self.base_prompt + Prompt.get_code_prompt(code) if is_first_prompt else self.base_prompt
        }

        return [system_template, base_template] if is_first_prompt else [base_template]
    
    @property
    @abstractmethod
    def base_prompt(self) -> str:
        """Base Prompt

        Returns:
            str: base prompt to use as instructions for GPT
        """
        pass


class Test(Prompt):
    @property
    def base_prompt(self) -> str:
        return f"""
Here is a code example: 
```csharp
{load_file('examples/CodeExample.cs')}
```
Here is the test for the code:
```csharp
{load_file('examples/TestExample.cs')}
```
Now, please generate unit test code for the given sample.
"""


class Format(Prompt):
    @property
    def base_prompt(self) -> str:
        return f"""
You need to modify the genedared code following these rules:
1. all using statements must be put within the namespace.
2. all using statements must follow alphabetical order.
3.`using System` must be put before all other using statements.
Here is an example: 
```csharp
{load_file('examples/FormatExample.cs')}
```
Now, please refine the given test code based on above rules. please do not change anything except for comments and using statements.
"""


class Comment(Prompt): 
    @property
    def base_prompt(self) -> str:
        return f"""
You must add comments over each [TestClass] and [TestMethod] attribute and class properties if they do not have.
You can refer to the example here: ```csharp\n{sample_comment}\n```
"""


class MoqToNSubstitute(Prompt):
    @property
    def base_prompt(self) -> str:
        return f"""
Here is a sample to convert Moq into NSubstitute. Moq: 
```csharp
{moq_sample}
```
NSubstitute: 
```csharp
{nsubstitute_sample}
```
Now, please replace Moq with NSubstitute for the given code.
"""