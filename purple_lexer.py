# Hal pertama yang dilakukan yaitu mengkonversi karakter menjadi token, hal ini disebut leksikal. Dipermudah dengan menggunakan SLY(Sly Lex Yacc)

from sly import Lexer

# Membangun class Lexer dari SLY, dan membuat kompiler yang membuat operasi aritmatika sederhana.

class PurpleLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, FOR, IF, THEN, TO, ELSE, FUN, EQEQ, ARROW, PRINT}
    literals = {'+', '-', '*', '/', '=', ',', ';', '(', ')'}
    ignore = ' \t'

# Menentukan token sebagai ekspresi reguler dan menyimpannya sebagai string

    FOR = r'UNTUK'
    IF = r'JIKA'
    THEN = r'MAKA'
    TO = r'KE'
    ELSE = r'LAIN'
    EQEQ = r'=='
    ARROW = r'->'
    FUN = r'SERU'
    PRINT= r'CETAK'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    # Number Token
    @_(r'\d+')
    def NUMBER(self,t):
        # mengkonversi kedalam bentuk integer
        t.value = int(t.value)
        return t

    # Comment Token
    @_(r'//.*') 
    def COMMENT(self, t):
        pass
    
    # New Line Token
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

if __name__ == '__main__':
    lexer = PurpleLexer()
    env = {}
    while True:
        try:
            text = input('Purple > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
