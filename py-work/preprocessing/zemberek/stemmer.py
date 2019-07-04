import inspect
import os
import jpype as jp
import atexit
import string

_initted = False
TurkishMorphology = None
RootLexicon = None
Paths = None
morphology = None

def stem_word(word):
    global _initted
    global TurkishMorphology
    global RootLexicon
    global Paths
    global morphology

    if _initted == False:
        # Import required Java classes
        TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
        RootLexicon = jp.JClass('zemberek.morphology.lexicon.RootLexicon')
        Paths = jp.JClass('java.nio.file.Paths')

        # Instantiating the morphology class with the default RootLexicon
        morphology = TurkishMorphology.createWithDefaults()
        _initted = True
    
    # Obtaining some results
    results = morphology.analyze(word).getAnalysisResults()
    root = results[0].getLemmas()[0] if results else ""
    return root

def stem_words(words):
    tokens = [stem_word(token) for token in words]
    return [token for token in tokens if token != ""]
