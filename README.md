# Password Strength Checker

A simple Python command-line tool that analyzes password strength.

## Features

* Hidden password input using `getpass`
* Detects:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Spaces
  * Special characters
* Password strength score (/5)
* Strength rating:

  * Very Weak
  * Weak
  * Medium
  * Strong
  * Very Strong

## Installation

Clone the repository:

```bash
git clone https://github.com/Anissa-Da/password-strength-checker.git
cd password-strength-checker
```

## Usage

Run the script:

```bash
python main.py
```

## Example

```text
=== Password Strength Checker ===
Enter password:

--- Password Analysis ---
Length       : 12
Lowercase    : 5
Uppercase    : 2
Digits       : 3
Spaces       : 0
Special chars: 2
Score        : 5/5
Strength     : Very strong password
```

## Technologies Used

* Python 3
* getpass
* string

## Author

Anissa HADJOU
