# tuMachine

Библиотека для генерации кода для машины Тьюринга

## Installation

To install the `tuMachine` library, you can use pip:

```
pip install tuMachine
```

## Usage

Here's an example of how to use the `tuMachine` library:

```python
from tuMachine import Constructor, Subtraction, SliceNumber

functions = [
    Subtraction(),
    SliceNumber([1, 2], 1, 0)
]

constructor = Constructor(functions, 3)
constructor.build("output.txt")
```

This code creates a Turing machine with two functions: Subtraction and SliceNumber. The `Constructor` class is used to combine these functions and generate the Turing machine code, which is then written to the `output.txt` file.

## API

The `tuMachine` library provides the following classes:

- `Function`: Base class for defining Turing machine functions.
- `Constructor`: Combines multiple functions to create a Turing machine.
- `CopySymbol`: Copies a symbol to a specified location.
- `CopyThroughtBeforeRight`: Copies a sequence of symbols before a specified symbol.
- `MoveThrought`: Moves the tape head through a sequence of symbols.
- `CopyThrought`: Copies a sequence of symbols to a specified location.
- `SliceNumber`: Extracts a slice of a number.
- `DeleteWordBeforeSymbol`: Deletes the word before a specified symbol.
- `Subtraction`: Implements subtraction.

Each class has its own set of methods and parameters that can be used to define the behavior of the Turing machine.

## Contributing

If you would like to contribute to the `tuMachine` library, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and add tests.
4. Submit a pull request.

## License

The `tuMachine` library is licensed under the MIT License.

## Testing

To run the tests for the `tuMachine` library, you can use the following command:

```
python -m unittest discover tests
```

This will run all the tests in the `tests` directory.