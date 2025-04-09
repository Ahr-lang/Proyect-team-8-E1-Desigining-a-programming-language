"""
Latin-to-Python Translator
---------------------------
This module provides functionality to convert Latin-like syntax
into valid Python code, supporting keywords, data types, operators,
and indentation for block structures.

Date: 9 April 2025
"""

import re

def translate_latin_to_python_line(code: str) -> str:
    """
    Translates a single line (or multi-line string) of Latin-style code
    into Python code, applying keyword substitution, operator mapping,
    and indentation tracking.

    Parameters:
        code (str): The Latin code string (may include escaped newlines)

    Returns:
        str: Translated and syntactically valid Python code
    """

    # Reserved keywords used in control flow and functions
    reserved_words = {
        'si': 'if',
        'aliter_si': 'elif',
        'alioquin': 'else',
        'dum': 'while',
        'pro': 'for',
        'definio': 'def',
        'redde': 'return',
        'experire': 'try',
        'nisi': 'except',
        'denique': 'finally',
        'eleva': 'raise',
        'asserere': 'assert',
        'praetere': 'pass',
        'rumpe': 'break',
        'perge': 'continue',
    }

    # Common data types and literals
    data_types = {
        'Verum': 'True',
        'Falsum': 'False',
        'Nullum': 'None',
        'integrare': 'int',
        'supernatet': 'float',
        'filum': 'str',
        'boolean': 'bool'
    }

    # Class/module related syntax
    class_module_system = {
        'classis': 'class',
        'importa': 'import',
        'ex': 'from',
        'ut': 'as',
        'universalis': 'global',
        'nonlocalis': 'nonlocal',
        'dele': 'del'
    }

    # Logical and comparison operators
    operators = {
        'et': 'and',
        'vel': 'or',
        'non': 'not',
        'est': 'is'
    }

    # Combine all mappings
    translation_map = {**reserved_words, **data_types, **class_module_system, **operators}

    # Convert escaped newline literals into actual newlines
    code = code.replace('\\n', '\n')
    translated_lines = []
    indent_level = 0

    # Keywords that dedent one level (else, elif, etc.)
    block_reset_keywords = {'elif', 'else', 'except', 'finally'}

    for line in code.split('\n'):
        # Tokenize the line (handles multi-character operators, words, and punctuation)
        tokens = re.findall(r'//|==|!=|<=|>=|\*\*|\\n|[^\w\s]|[\w]+', line)
        translated_tokens = [translation_map.get(token, token) for token in tokens]

        # Detect dedent trigger by first word
        first_token = next((t for t in translated_tokens if t.strip()), '')
        if first_token in block_reset_keywords and indent_level > 0:
            indent_level -= 1

        # Reconstruct the line with correct spacing
        translated_line = ''
        for i, token in enumerate(translated_tokens):
            if token in {'(', ')', '[', ']', '{', '}', ',', ':', '.', ';'}:
                translated_line += token
            elif i > 0 and translated_tokens[i - 1] not in {'(', '[', '{', ',', ':', '.', ';'}:
                translated_line += ' ' + token
            else:
                translated_line += token

        # Add indentation
        current_indent = '    ' * indent_level
        translated_lines.append(current_indent + translated_line)

        # Increase indent level if the line ends in a colon
        if translated_line.strip().endswith(':'):
            indent_level += 1

    # Join all lines into a full translated Python block
    full_code = '\n'.join(translated_lines)

    # Fix exponentiation spacing: '* *' → '**'
    full_code = re.sub(r'\* \*', '**', full_code)

    # Fix scientific notation spacing: '1.6e - 19' → '1.6e-19'
    full_code = re.sub(r'(\d+(?:\.\d+)?[eE])\s*([+-])\s*(\d+)', r'\1\2\3', full_code)

    return full_code


def translate_file(input_path: str, output_path: str):
    """
    Reads a Latin-style code file line-by-line, translates each line to Python,
    and writes the result to a new file.

    Parameters:
        input_path (str): Path to the original Latin input file
        output_path (str): Path where the translated Python file will be saved
    """
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            translated_line = translate_latin_to_python_line(line.strip())
            outfile.write(translated_line + '\n')
