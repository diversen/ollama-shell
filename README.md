# ollama-shell

Ask a shell question and get a command to execute.

## Install
<!-- LATEST-VERSION-PIPX -->
	pipx install git+https://github.com/diversen/ollama-shell@v0.1.1

## Generate a config file

You will need to choose a valid ollama model that exists on your system.

    ollama-shell

Now you can choose a model from all the models that are available on your system.

E.g.: 

    Select a model from the following list:
    codegeex4:latest
    llama3.2:latest

`codegeex4:latest` will work great for shell commands.

Copy and paste the model you want to use into the config file. The config file is located in `~/.config/ollama-shell/config.yaml`.

## Ask a question

Now ask a question:

    ollama-shell -q "find all json files in current folder"

The above command may return something like this:

    This command searches for JSON files in the current directory and its
    subdirectories. The '.' specifies the current directory, '-type f' indicates
    that we are looking for files, and '-name '*.json'' filters for files with a
    '.json' extension.

    This following command has been copied to your clipboard:

    find . -type f -name '*.json'

If you are satisfied with the answer you can press `Ctrl + Shift + V` to paste the command into your terminal.

## Reset config

    ollama-shell -c

## License

MIT
