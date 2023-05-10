# README

## Talk to chatgpt API using python

This is a basic python script that calls chatgpt api to get python code for the task that we specify and saves to the file given.

Pre-requisite:

- Install python requests module using pip

```bash
pip3 install requests
```

- Export variable

```bash
export OPENAI_API_KEY=<openai api key>
```

## Usage

syntax:

```bash
python3 chatgpt-python.py < Task to do > < output file >
```

example:

```bash
python3 chatgpt-python.py "print current date" "print_date.py"
```

This will save the code necessary for the task (`print current date`) to file `print_date.py`.
Later take a look to the code whether it is correct and run it.

```bash
python3 print_date.py
```
