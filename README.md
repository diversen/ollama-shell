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

Now ask a question:

    ollama-shell -q "Using apt how do I search for a package on linux?"

The above command may return something like this:

    Replace '<package_name>' with the name of the package you are searching for.
    This command will return a list of packages that match your search query.

    This following command has been copied to your clipboard:

    apt-cache search <package_name>

If you are satisfied with the answer you can press `Ctrl + Shift + V` to paste the command into your terminal.

## Reset config

    ollama-shell -c

## License

MIT
# ollama-shell
# ollama-shell
