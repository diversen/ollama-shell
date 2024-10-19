import ollama
import argparse
import os
import platform
import json
import appdirs
import pyperclip
import textwrap
import re
import yaml
from colorama import Fore, Style, init


init()


app_dir = appdirs.user_data_dir("ollama_shell")
app_config_file = os.path.join(app_dir, "config.yaml")

prompt_template = """
Your response should be a JSON object given as a string.
You response may only be a valid JSON object.

You job is to create a shell command from a question.
The command should work on: {system_name}. The shell where the command will be used is: {shell_name}.

Any comments should be added to the key "comments" in the JSON object.
Your "command" should be added to the key "command" in the JSON object. 
You "command" should always provide an executable command that can be copy-pasted into the terminal.

This is the question: {question}"""

model = "codegeex4"
temperature = 0.3

config = {
    "model": model,
    "prompt_template": prompt_template,
    "temperature": temperature,
}

if not os.path.exists(app_dir):
    os.makedirs(app_dir)


def get_models() -> list:
    models = ollama.list()
    return models.get("models")


def print_common(text: str):

    if isinstance(text, list):
        text = " ".join(text)

    # max width is 80
    text = textwrap.fill(text, width=80)
    print(text)


def print_command(text: str):
    print(Fore.GREEN + text + Fore.RESET)


def write_default_config():
    if not os.path.exists(app_config_file):

        print_common("Select model from the following list:")
        models = get_models()
        
        for model in models:
            print_common(model["name"])
        
        # read model from user
        print()
        model = input("Enter model name to use: ")

        # check if model is valid
        if model not in [m["name"] for m in models]:
            print_common("Invalid model")
            exit(1)

        print()
        config["model"] = model


        os.makedirs(app_dir, exist_ok=True)
        with open(app_config_file, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
            print("Writing config file to:\n")
            print_command(app_config_file)
            print()

write_default_config()

# Load config file
with open(app_config_file, "r") as f:
    config = yaml.safe_load(f)
    model = config["model"]
    prompt_template = config["prompt_template"]
    temperature = config["temperature"]


def get_prompt_text(question: str):

    system_name = platform.system()

    # get shell name if unix
    if system_name == "Linux" or system_name == "Darwin":
        shell_name = os.environ["SHELL"]

    # get shell name if windows
    if system_name == "Windows":
        shell_name = os.environ["ComSpec"]

    prompt = prompt_template.format(
        system_name=system_name, shell_name=shell_name, question=question
    )

    return prompt


def get_args():
    """Get the CLI arguments"""

    parser = argparse.ArgumentParser(description="Get a command by asking ollama-shell")
    parser.add_argument(
        "-q",
        "--question",
        type=str,
        help="The question to ask ollama-shell",
    )

    # add clear config option
    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
        help="Reset config file",
    )

    args = parser.parse_args()

    if args.clear:
        os.remove(app_config_file)
        print("Config file removed")
        exit()

    if args.question is None:
        print("Please provide a question to ask ollama-shell")
        exit()

    return args


def get_prompt(args: argparse.Namespace):

    prompt = get_prompt_text(args.question)

    # ask the question
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        options={"temperature": temperature},
    )

    return response


def extract_code_blocks(text):
    # Regular expression to match text between ``` or ```json markers
    pattern = r"```(?:json\n|\n)?(.*?)```"

    # Find all matches in the text using re.DOTALL to capture newlines
    code_blocks = re.findall(pattern, text, re.DOTALL)

    return code_blocks


def get_clean_response(response):
    text_response: str = response["message"]["content"]

    # Check if the response is a valid JSON string
    try:
        json_response = json.loads(text_response)
        return json_response
    except Exception as e:
        pass

    # Try to extract code blocks from the response
    code_blocks = extract_code_blocks(text_response)
    if code_blocks:

        try:
            json_response = json.loads(code_blocks[0])
            return json_response
        except Exception as e:
            pass

    return


def main():
    args = get_args()
    response = get_prompt(args)
    json_response = get_clean_response(response)

    if not json_response:
        print("No valid JSON response")
        print(response)
        exit()

    # check if a comment is provided
    if "comments" in json_response:
        print_common(json_response["comments"])
        print()

    # check if an answer is provided
    if "command" in json_response:
        print_common("This following command has been copied to your clipboard:")
        print()
        print_command(json_response["command"])

        pyperclip.copy(json_response["command"])

    exit(0)
