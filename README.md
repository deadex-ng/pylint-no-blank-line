# Pylint-no-blank-line
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

This is a pylint-plugin that ensures that there's no blank line after function definition.

## Examples
Good:

```
def multiply(x: int, y: int) -> int:
    """multiply two numbers."""
    return x*y
```
Bad:
```
def multiply(x: int, y: int) -> int:
    """multiply two numbers."""

    return x*y
```
## Installation
```
pip install pylint_no_blank_line
```
## How to use it

```
pylint --load-plugins=pylint_no_blank_line <FILE TO CHECK>
```

Not done
