import inspect
import os
import jpype as jp
import atexit
import string

# Adjust the working directory
module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))
os.chdir(module_dir)

# Relative path to Zemberek .jar
ZEMBEREK_PATH = 'bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import the required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
TurkishSentenceNormalizer = jp.JClass('zemberek.normalization.TurkishSentenceNormalizer')
Paths = jp.JClass('java.nio.file.Paths')

# Get the path to the (baseline) lookup files
lookupRoot = Paths.get('data/normalization')

# Get the path to the compressed bi-gram language model
lmPath = Paths.get('data/lm/lm.2gram.slm')

# Instantiate the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

# Initialize the TurkishSentenceNormalizer class
normalizer = TurkishSentenceNormalizer(morphology, lookupRoot, lmPath)

def normalize(text):
	text = normalizer.normalize(text)
	text = text.translate(str.maketrans('', '', string.punctuation))
	while '  ' in text:
		text = text.replace('  ', ' ')
	return text

def shutdown():
	jp.shutdownJVM()

atexit.register(shutdown)