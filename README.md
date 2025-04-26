# Random Password Generator 🔐

This is a simple Python script that generates a random 8-character password using a mix of lowercase letters, uppercase letters, digits, and punctuation symbols.

## Features

- Generates a random 8-character password
- Uses:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Numbers (`0-9`)
  - Punctuation symbols (`!@#$%^&*()`, etc.)

## How It Works

The script builds a character pool from:
- `string.ascii_lowercase`
- `string.ascii_uppercase`
- `string.digits`
- `string.punctuation`
- (Note: `string.ascii_letters` is redundant here since it's already included in uppercase and lowercase)

Then it selects 8 characters at random from the pool to form a password.

## Usage

1. Make sure you have Python installed.
2. Run the script:

```bash
python password_generator.py
