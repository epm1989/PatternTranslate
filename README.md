
# Alert Logic

## Run, built in python3.8

- Sample file, run next line in console to create the file.
```shell
echo -e "foo blah is a bar
foo blah is a bar and large thins is
foo blah is a very big boat
foo blah is a very big boat and under the sea
foo blah is bar
foo blah
foo blah is" > input.txt
```

- Execution
```bash
cat input.txt | python main.py "foo %{0} is a %{1}" > output.txt
```

`1. Check results in output.txt`
`2. Check logs as a STDERR output in console`

## Install as a package
```bash
pip install -e .
```

### Verify installation
```bash
pip freeze
# Editable install with no version control (pattern-translate==1.0.1)
-e /{{working_directory}}/
```

### Use as a module
```python
from pattern_translate import PatternTranslate
pattern = "foo %{0} is a %{1}" 

# you could have  either a list of string or a paragraph or even a single string as a input, as shown below.
lines  = 'foo blah is a bar'

lines = """foo blah is a bar
foo blah is a very big boat
foo blah is bar
foo blah
foo blah is"""

lines = ['foo blah is a bar', 'foo blah is a very big boat', 'foo blah is bar', 'foo blah', 'foo blah is']

alert = PatternTranslate(pattern, lines)
alert.fetch_lines()
print(alert.output)
['foo blah is a bar', 'foo blah is a very big boat']
```


