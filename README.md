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
from tuMachine import *

left_two_numbers = MoveThrought(2,0)
copy_num = CopyThrought(2,1,1)

c = Constructor([left_two_numbers,copy_num],2)
c.build('tuCode.txt')
```

This code creates a Turing machine with two functions: MoveTrought and CopyThrought. The `Constructor` class is used to combine these functions and generate the Turing machine code, which is then written to the `tuCode.txt` file.

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
- `Subtraction`: Implements subtraction. <- in procces

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
