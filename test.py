from translator import translate_file
from arithmetic_lexer import lexicalAnalyzer

if __name__ == "__main__":
    # Latin Txt Files
    input_latin = "./txt_files/latin_input.txt"
    translated_file = "./txt_files/translated_file.txt"

    translate_file(input_latin, translated_file)
    print(f"Translated {input_latin} → {translated_file}")

    # Arithmetic Lexer
    input_arithmetic = "./txt_files/translated_file.txt"
    output_arithmetic = "./txt_files/arithmetic_output.txt"

    lexicalAnalyzer(input_arithmetic, output_arithmetic)
    print(f"Arithmetic Lexer: {input_arithmetic} → {output_arithmetic}")