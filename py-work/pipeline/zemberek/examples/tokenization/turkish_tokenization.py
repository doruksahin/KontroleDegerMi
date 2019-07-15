# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Tokenization Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/tokenization
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/tokenization/TurkishTokenizationExample.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (ZEMBEREK_PATH))

# Import required Java classes
TurkishTokenizer = jp.JClass('zemberek.tokenization.TurkishTokenizer')
TurkishLexer = jp.JClass('zemberek.tokenization.antlr.TurkishLexer')

# There are static instances provided for common use:
    # DEFAULT tokenizer ignores most white spaces (space, tab, line feed and carriage return).
    # ALL tokenizer tokenizes everything.
tokenizer = TurkishTokenizer.ALL

# A dummy data to work on
dummy = "Prof. Dr. Veli Davul açıklama yaptı. Kimse %6.5'lik enflasyon oranını beğenmemiş!"

# Creating the TokenIterator instance
tokenIterator = tokenizer.getTokenIterator(dummy)

# Iterating through the tokens using the TokenIterator instance
while (tokenIterator.hasNext()):
    # Setting the current token
    try:
        token = tokenIterator.next()
    except StopIteration:
        break
    
    # Printing the token information
    print('Token = ' + str(token.getText()) 
        + ' | Type (Raw) = ' + str(token.getType()) 
        + ' | Type (Lexer) = ' + str(token.getType())
        + ' | Start Index = ' + str(token.getStart()) 
        + ' | Ending Index = ' + str(token.getEnd())
    )

jp.shutdownJVM()