# ollama-shell

Ask a shell question and get a command to execute.

Example: 

    ollama-shell -q "put the string 'test' into a file named test.txt"

Will respond with something like this:

    This command will create a new file named test.txt and write the string 'test'
    into it. If the file already exists, its contents will be overwritten.

    This following command has been copied to your clipboard:

    echo 'test' > test.txt

## Install
<!-- LATEST-VERSION-PIPX -->
	pipx install git+https://github.com/diversen/ollama-shell@v0.1.1

## Generate a config file

On first usage you will need to choose a valid ollama model that exists on your system:

    ollama-shell

E.g.:

    Select a model from the following list:
    codegeex4:latest
    llama3.2:latest

`codegeex4:latest` will work great for shell commands.

Paste your chosen model and press return. The config file has been written and saved.
On my system it is saved in the following location: 

    ~/.local/share/ollama_shell/config.yaml 

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
