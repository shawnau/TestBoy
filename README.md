# TestBoy
TestBoy writes unit tests for your code using GPT prompt chaining, which means you can combine different prompts to solve complex tasks, or use them individually.
It will also retrieve related document from your documents to instruct GPT for your query.


```text
query ---> query+doc ---> GPT
  |            ^
  |            |
  v            |
documents vector DB
```

# Install

```bash
pip install -r requirements.txt
```

# Settings
Please refer to [config.yaml](config.yaml)

# Usage

```python
import testboy
# initialize settings from config.yaml
testboy.config('config.yaml')

from testboy.session import Session

# set input and output to paths of the code
Session(code_paths=['CodeExample.cs']).execute([
    "Write unit tests for the code.", # first, write the test
    "Format the tests.", # then, format the code according your use
    "Add comment for the tests." # finally, add comments
]).dump('CodeExampleTest.cs')
```

For more details, please refer to the [example.ipynb](example.ipynb)
