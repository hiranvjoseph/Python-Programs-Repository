# Python Programs Repository

Welcome to the Python Programs Repository by Hiran Joseph.

## Introduction
This repository is a collection of Python programs that cover a wide range of topics and functionalities. Each directory within this repository represents a specific program or project. In this directory, we have a simple yet useful program that generates random passwords using Python.

## Password Generator
### Directory: [Password_Generator](https://github.com/hiranvjoseph/Python-Programs-Repository/blob/main/Password_Generator)

- **Program:** [passwordGenarator.ipynb](https://github.com/hiranvjoseph/Python-Programs-Repository/Password_Generator/PasswordGenarator.ipynb)

The "Password Generator" program is designed to create random passwords using Python. It utilizes the `random` and `string` libraries to generate strong and unpredictable passwords. The generated passwords can be customized in terms of length and complexity.

### How to Generate a New Password

To generate a new password, follow these steps:

1. Open the `PasswordGenarator.ipynb` file in your Jupyter Notebook or Python environment.

2. Run the code in the notebook.

3. When prompted, type the command 'new password' and press Enter.

4. The program will generate a random password and display it.

### Example Usage
python
# Example Usage
# Import the required libraries
import random
import string

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a new password
command = input("Type 'new password' to generate a new password: ")
if command == 'new password':
    password = generate_password()
    print("Generated Password:", password)
else:
    print("Invalid command. Please type 'new password' to generate a new password.")


## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
If you'd like to contribute your own Python programs or have ideas for new projects, please feel free to open an issue or submit a pull request. Your contributions and ideas are highly valued.

## Contact
- **Hiran Joseph**
- **Email**: [hiranvjoseph@gmail.com](mailto:hiranvjoseph@gmail.com)

Explore and use Python programs in this repository for various functionalities, and feel free to contribute and share your own projects. Happy coding!
