import re

def is_float(string):
    return re.fullmatch(r'[+-]?(\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?', string) is not None

def is_integer(string):
    return re.fullmatch(r'[+-]?\d+(_\d+)*', string) is not None

def is_variable(string):
    return re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', string) is not None

def is_boolean(string):
    return string in ['True', 'False']

def is_keyword(string):
    return string in ['def', 'return', 'print', 'if', 'else', 'elif', 'while', 'for', 'in', 'break', 'continue']

def is_logical_operator(string):
    return string in ['and', 'or', 'not']

def lexicalAnalyzer(input_path, output_path):
    # Map of single-character operators and punctuation
    token_map = {
        '=': 'Assignment',
        '+': 'Addition',
        '-': 'Subtraction',
        '*': 'Multiplication',
        '/': 'Division',
        '^': 'Power',
        '(': 'Open Parenthesis',
        ')': 'Close Parenthesis',
        '[': 'Open Bracket',
        ']': 'Close Bracket',
        '{': 'Open Brace',
        '}': 'Close Brace',
        ':': 'Colon',
        ',': 'Comma',
        '.': 'Dot',
        '<': 'Less Than',
        '>': 'Greater Than'
    }

    # Multi-character operators
    multi_char_ops = {
        '<=': 'Less Than or Equal',
        '>=': 'Greater Than or Equal',
        '==': 'Equal To',
        '!=': 'Not Equal'
    }

    # Regex patterns
    float_pattern = re.compile(r'[+-]?(\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?')
    int_pattern = re.compile(r'[+-]?\d+(_\d+)*')
    var_pattern = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
    string_pattern = re.compile(r'("([^"\\]|\\.)*")|(\'([^\'\\]|\\.)*\')')

    with open(input_path, 'r') as f:
        lines = f.readlines()

    with open(output_path, 'w') as out:
        out.write("Lexical Analysis Output:\n\n")
        for linenum, line in enumerate(lines, 1):
            original_line = line.rstrip('\n')
            line = line.strip()
            if not line:
                continue
            out.write(f"LINE {linenum}: {original_line}\n")

            if line.startswith('//'):
                out.write("{:<22}{}\n".format("Comment", original_line))
                continue

            idx = 0
            while idx < len(line):
                if line[idx].isspace():
                    idx += 1
                    continue

                if line[idx:idx+2] == '//':
                    out.write("{:<22}{}\n".format("Comment", line[idx:].strip()))
                    break

                # Multi-character operators (==, !=, <=, >=)
                matched_multi_op = False
                for op, label in multi_char_ops.items():
                    if line[idx:idx+len(op)] == op:
                        out.write("{:<22}{}\n".format(label, op))
                        idx += len(op)
                        matched_multi_op = True
                        break
                if matched_multi_op:
                    continue

                # String literals
                string_match = string_pattern.match(line[idx:])
                if string_match:
                    token = string_match.group()
                    out.write("{:<22}{}\n".format("String", token))
                    idx += len(token)
                    continue

                # Float
                float_match = float_pattern.match(line[idx:])
                if float_match:
                    token = float_match.group().replace("_", "")
                    out.write("{:<22}{}\n".format("Float", token))
                    idx += len(token)
                    continue

                # Integer
                int_match = int_pattern.match(line[idx:])
                if int_match:
                    token = int_match.group().replace("_", "")
                    out.write("{:<22}{}\n".format("Integer", token))
                    idx += len(token)
                    continue

                # Variable / keyword / boolean / logical
                word_match = var_pattern.match(line[idx:])
                if word_match:
                    token = word_match.group()
                    if is_boolean(token):
                        out.write("{:<22}{}\n".format("Boolean", token))
                    elif is_keyword(token):
                        out.write("{:<22}{}\n".format("Keyword", token))
                    elif is_logical_operator(token):
                        out.write("{:<22}{}\n".format("Logical Operator", token))
                    else:
                        out.write("{:<22}{}\n".format("Variable", token))
                    idx += len(token)
                    continue

                # Known single-character operator or punctuation
                if line[idx] in token_map:
                    out.write("{:<22}{}\n".format(token_map[line[idx]], line[idx]))
                    idx += 1
                    continue

                # Escape sequence (e.g., \n, \t)
                if line[idx] == '\\' and idx + 1 < len(line):
                    out.write("{:<22}{}\n".format("Escape Sequence", line[idx:idx+2]))
                    idx += 2
                    continue

                # Anything else is unrecognized
                out.write("{:<22}{}\n".format("Unrecognized", line[idx]))
                idx += 1
