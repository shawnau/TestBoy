import argparse
from prompts import Test, Comment, MoqToNSubstitute, Format
from context import Context

def comment(input, output):
    context = Context([input])
    context.prompt_chaining([
        Comment()
    ])
    context.dump(output)

def test(input, output):
    # without deps. use Context([code, dep1, dep2, ...]) if you have deps
    context = Context([input])
    context.prompt_chaining([
        Test(),
        Format(),
        Comment()
    ])
    context.dump(output)

def unmoq(input, output):
    context = Context([input])
    context.prompt_chaining([
        MoqToNSubstitute()
    ])

    context.dump(output)

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="TestBoy have 3 commands: test, comment and unmoq. \n example: python testboy.py test input.cs --output.cs")

    # Add positional argument for the command
    parser.add_argument("command", choices=["test", "comment", "unmoq"], help="The command to run")

    # Add positional argument for the filepath
    parser.add_argument("input", help="The file to process")

    # Add optional argument for the output path
    parser.add_argument("--output", help="Optional output file path. If not specified, it will replace input inplace")

    # Parse the command-line arguments
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else args.input
    
    # Switch behavior based on the command argument
    if args.command == "test":
        if input_file == output_file:
            output_file = input_file.replace('.cs', 'Tests.cs')
        test(input_file, output_file)
    elif args.command == "comment":
        comment(input_file, output_file)
    elif args.command == "unmoq":
        unmoq(input_file, output_file)
