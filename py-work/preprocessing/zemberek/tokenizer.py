####import inspect
####import os
####import jpype as jp
####import atexit
####import string
####
##### Adjust the working directory
####module_path = inspect.getfile(inspect.currentframe())
####module_dir = os.path.realpath(os.path.dirname(module_path))
####os.chdir(module_dir)
####
##### Relative path to Zemberek .jar
####ZEMBEREK_PATH = 'bin/zemberek-full.jar'
####
##### Start the JVM
####jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (ZEMBEREK_PATH))
####
##### Import required Java classes
####TurkishTokenizer = jp.JClass('zemberek.tokenization.TurkishTokenizer')
####TurkishLexer = jp.JClass('zemberek.tokenization.antlr.TurkishLexer')
####
##### There are static instances provided for common use:
####    # DEFAULT tokenizer ignores most white spaces (space, tab, line feed and carriage return).
####    # ALL tokenizer tokenizes everything.
####tokenizer = TurkishTokenizer.DEFAULT
####
####def tokenize(text):
####    # Creating the TokenIterator instance
####    tokenIterator = tokenizer.getTokenIterator(text)
####
####    # Iterating through the tokens using the TokenIterator instance
####    while (tokenIterator.hasNext()):
####        # Setting the current token
####        try:
####            token = tokenIterator.next()
####        except StopIteration:
####            break
####        
####        # Printing the token information
####        print('Token = ' + str(token.getText()) 
####            + ' | Type (Raw) = ' + str(token.getType()) 
####            + ' | Type (Lexer) = ' + str(token.getType())
####            + ' | Start Index = ' + str(token.getStart()) 
####            + ' | Ending Index = ' + str(token.getEnd())
####        )
####
####def _shutdown():
####	jp.shutdownJVM()
####
####atexit.register(_shutdown)
####
####tokenize("Prof. Dr. Veli Davul açıklama yaptı. Kimse %6.5'lik enflasyon oranını beğenmemiş!")