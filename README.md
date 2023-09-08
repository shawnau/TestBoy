# TestBoy
TestBoy writes unit tests for your code using GPT prompt chaining.
It can actually do more than just testing if you write prompts! And it's easy to extend!

# Requirements

1. [Python](https://www.python.org/) >= 3.10
3. [openai python sdk](https://github.com/openai/openai-python)

# Setting up openai key and endpoint
you can set them through the environment variables.

# Usage
```python
# test code, will generate test file with filename = CodeExampleTests.cs
python testboy.py test examples\CodeExample.cs

# in-place add comments to your code
python testboy.py comment examples\CodeExample.cs

# in-place convert Moq to NSubstitute
python testboy.py unmoq examples\MoqExample.cs

```

# Customize
You can easily customize via writing new Prompts, here's an example:
in [prompts.py][prompts.py], add a new class called `RemoveApple` which inherits `Prompt`

```python
class RemoveApple(Prompt):
    @property
    def base_prompt(self) -> str:
        return f"""We define apple as a bad word. Please remove or rename it in the given code."""
```

then, just call it!

```python
def bad_apple(input, output):
    context = Context([input])
    context.prompt_chaining([
        RemoveApple()
    ])
    context.dump(output)
```