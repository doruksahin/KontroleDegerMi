#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import os
import jpype as jp
import atexit
import string

init = False
TurkishMorphology = None
RootLexicon = None
Paths = None
morphology = None

#NOT:
#Kitabı -> kitab olarak alıyor. Son harfi yumuşak bırakıyor. Düzeltilebilir.
def stem_word(word):
    global init
    global TurkishMorphology
    global RootLexicon
    global Paths
    global morphology

    if init == False:
        # Import required Java classes
        TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
        RootLexicon = jp.JClass('zemberek.morphology.lexicon.RootLexicon')
        Paths = jp.JClass('java.nio.file.Paths')

        # Instantiating the morphology class with the default RootLexicon
        morphology = TurkishMorphology.createWithDefaults()
        init = True
    
    # Obtaining some results
    results = morphology.analyze(word).getAnalysisResults()
    root = results[0].getLemmas()[0] if results else ""
    return root

def stem_words(words):
    tokens = [stem_word(token) for token in words]
    return [token for token in tokens if token != ""]
