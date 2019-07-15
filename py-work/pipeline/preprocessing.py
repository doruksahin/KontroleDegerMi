#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
import tokenizer, zemberek.normalizer, zemberek.stemmer, stopper

def perform_preprocessing(text):
	text = zemberek.normalizer.normalize(text)
	tokens = tokenizer.tokenize(text)
	tokens = stopper.remove_stops(tokens)
	tokens = zemberek.stemmer.stem_words(tokens)
	tokens = stopper.remove_stops(tokens)
	return tokens

