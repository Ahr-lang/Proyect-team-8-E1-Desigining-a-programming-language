# E1 Project – Custom Latin-Based Programming Language

Date: 9 April 2025

This project implements a custom programming language that uses Latin-based syntax. It includes a complete pipeline for translating the code to Python, performing lexical analysis using regular expressions, and performing syntactic analysis using Python's Abstract Syntax Tree (AST) module.

---

## Overview

The system follows three main stages:

1. **Translation**  
   Latin-like keywords and expressions are translated to valid Python syntax using `translator.py`.

2. **Lexical Analysis**  
   Tokens such as keywords, identifiers, operators, numbers, and strings are identified using the `lexicalAnalyzer` function in `arithmetic_lexer.py`.

3. **Syntactic Analysis**  
   Code blocks are parsed using the `ast` module to verify that the translated code conforms to Python syntax. This is handled in `ast_analysis.py`.

---

## File Descriptions

### Source Files

- `translator.py`  
  Translates Latin-like code into Python syntax. Handles keyword replacements, indentation, exponentiation, and formatting of scientific notation.

- `arithmetic_lexer.py`  
  Performs lexical analysis using regular expressions. Recognizes keywords, logical operators, numeric literals, variables, string literals, and special characters.

- `ast_analysis.py`  
  Parses translated code using Python's AST module. Also includes example test expressions and the required `syntacticAnalyzer(inputFile, outputFile)` function.

- `test.py`  
  Main script that executes the full process: translation, lexical analysis, and syntactic analysis.

---


