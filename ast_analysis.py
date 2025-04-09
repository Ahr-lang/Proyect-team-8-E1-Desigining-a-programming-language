"""
AST Analysis and Syntactic Validator
------------------------------------
Parses and analyzes translated Python code using the built-in AST module.
Visualizes AST trees for Latin-based expressions and performs syntax validation.

Date: 9 April 2025
"""

import ast
from translator import translate_latin_to_python_line

# --------------------------------------------------
# AST Visualization for Translated Latin Code Blocks
# --------------------------------------------------

def explore_ast_latin(latin_code, label=""):
    """
    Translates a Latin-like expression to Python, prints both versions,
    and outputs the corresponding AST structure.
    """
    print(f"\n--- {label} ---")
    print("Original (Latin):")
    print(latin_code)

    # Translate to Python
    python_code = translate_latin_to_python_line(latin_code)
    print("\nTranslated (Python):")
    print(python_code)

    # Parse and display AST
    tree = ast.parse(python_code)
    print("\nAST:")
    print(ast.dump(tree, indent=4))
    return tree

# ---------------------- LATIN EXPRESSION EXAMPLES ----------------------

latin_expr1 = "total = a + b * (c - d)"
latin_expr2 = "result = (a + b) * (c - d) / e"
latin_expr3 = "si Verum et non Falsum:\n    redde 'correxit'"
latin_expr4 = (
    "si x < y:\n"
    "    redde x\n"
    "aliter_si x > y:\n"
    "    redde y\n"
    "alioquin:\n"
    "    redde Nullum"
)
latin_expr5 = "dum n > 1:\n    n = n - 1"
latin_expr6 = "pro i in range(5):\n    print(i)"
latin_expr7 = (
    "definio comparare(x, y):\n"
    "    si x == y:\n"
    "        redde Verum\n"
    "    alioquin:\n"
    "        redde Falsum"
)
latin_expr8 = "duplicare = lambda x: x * 2"
latin_expr9 = (
    "definio affirmatio(v):\n"
    "    si v est Verum:\n"
    "        redde 'affirmatum'\n"
    "    alioquin:\n"
    "        redde 'negatum'"
)
latin_expr10 = "menssage = 'resultat: ' + str(5 + 3)"

# ---------------------- AST TESTS ----------------------

explore_ast_latin(latin_expr1, "Expr 1: Arithmetic")
explore_ast_latin(latin_expr2, "Expr 2: Grouped Arithmetic")
explore_ast_latin(latin_expr3, "Expr 3: Boolean Condition")
explore_ast_latin(latin_expr4, "Expr 4: Conditional Branching")
explore_ast_latin(latin_expr5, "Expr 5: While Loop")
explore_ast_latin(latin_expr6, "Expr 6: For Loop")
explore_ast_latin(latin_expr7, "Expr 7: Function Definition")
explore_ast_latin(latin_expr8, "Expr 8: Lambda Expression")
explore_ast_latin(latin_expr9, "Expr 9: Function w/ Boolean Check")
explore_ast_latin(latin_expr10, "Expr 10: String + Arithmetic")

# ---------------------- SYNTAX ANALYZER FUNCTION ----------------------

def syntacticAnalyzer(inputFile: str, outputFile: str) -> None:
    """
    Reads a translated Python file, breaks it into code blocks,
    parses each block using the AST module, and records whether
    each block is syntactically valid.

    Parameters:
    - inputFile: path to the translated file
    - outputFile: path to write the True/False validity per block
    """
    with open(inputFile, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks = []
    current_block = []

    # Group lines into code blocks (split by blank lines)
    for line in lines:
        if line.strip() == "":
            if current_block:
                blocks.append("".join(current_block))
                current_block = []
        else:
            current_block.append(line)

    if current_block:
        blocks.append("".join(current_block))

    # Write syntactic validity results
    with open(outputFile, 'w', encoding='utf-8') as out:
        out.write("Syntactic Analysis Results:\n\n")
        for i, block in enumerate(blocks, 1):
            try:
                ast.parse(block)
                valid = True
            except SyntaxError:
                valid = False
            out.write(f"Expression {i}:\n{block}Valid: {valid}\n\n")

# ---------------------- AST NODE INSPECTOR ----------------------

def list_node_types(code):
    """
    Utility function to return all unique AST node types in a code snippet.
    """
    tree = ast.parse(code)
    return sorted(set(type(node).__name__ for node in ast.walk(tree)))

print("\nUnique AST node types in arithmetic expression:")
print(list_node_types("total = a + b * (c - d)"))
