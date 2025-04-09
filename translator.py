import re

def translate_latin_to_python_line(code: str) -> str:
    # Define translation maps
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

    data_types = {
        'Verum': 'True',
        'Falsum': 'False',
        'Nullum': 'None',
        'integrare': 'int',
        'supernatet': 'float',
        'filum': 'str',
        'boolean': 'bool'
    }

    class_module_system = {
        'classis': 'class',
        'importa': 'import',
        'ex': 'from',
        'ut': 'as',
        'universalis': 'global',
        'nonlocalis': 'nonlocal',
        'dele': 'del'
    }

    operators = {
        'et': 'and',
        'vel': 'or',
        'non': 'not',
        'est': 'is'
    }

    # Combine all translation maps
    translation_map = {**reserved_words, **data_types, **class_module_system, **operators}

    # Tokenize the input code
    tokens = re.findall(r'//|\\n|\\t|[^\w\s]|[\w]+', code)

    # Translate tokens
    translated_tokens = [translation_map.get(token, token) for token in tokens]

    # Join tokens with appropriate spacing
    translated_code = ''
    for i, token in enumerate(translated_tokens):
        if token in {'\n', '\t', '(', ')', '[', ']', '{', '}', ',', ':', '.', ';'}:
            translated_code += token
        elif i > 0 and translated_tokens[i - 1] not in {'\n', '\t', '(', '[', '{', ',', ':', '.', ';'}:
            translated_code += ' ' + token
        else:
            translated_code += token

    return translated_code

def translate_file(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            translated_line = translate_latin_to_python_line(line.strip())
            outfile.write(translated_line + '\n')