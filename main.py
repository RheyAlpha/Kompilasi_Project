import purple_lexer
import purple_parser
import purple_interpreter

from sys import *

lexer = purple_lexer.PurpleLexer()
parser = purple_parser.PurpleParser()
env = {}

file  = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    purple_interpreter.PurpleExecute(tree, env)