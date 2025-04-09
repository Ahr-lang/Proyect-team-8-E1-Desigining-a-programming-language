"""
Main Execution Script
---------------------
This script runs the full pipeline:
1. Translates Latin-style code into Python
2. Performs lexical analysis
3. Performs syntactic analysis

Date: 9 April 2025
"""

from translator import translate_file
from arithmetic_lexer import lexicalAnalyzer
from ast_analysis import syntacticAnalyzer

if __name__ == "__main__":
    # ------------------- Translation -------------------
    input_latin = "./txt_files/latin_input.txt"
    translated_file = "./txt_files/translated_file.txt"

    translate_file(input_latin, translated_file)
    print(f"Translated {input_latin} → {translated_file}")

    # ------------------- Lexical Analysis -------------------
    input_arithmetic = translated_file
    output_arithmetic = "./txt_files/arithmetic_output.txt"

    lexicalAnalyzer(input_arithmetic, output_arithmetic)
    print(f"Lexical Analysis: {input_arithmetic} → {output_arithmetic}")

    # ------------------- Syntactic Analysis -------------------
    input_syntax = translated_file
    syntax_results = "./txt_files/syntax_results.txt"

    syntacticAnalyzer(input_syntax, syntax_results)
    print(f"Syntactic results written to {syntax_results}")
