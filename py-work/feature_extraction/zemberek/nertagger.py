#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import os
import jpype as jp
import atexit
import string

init = False
TurkishMorphology = None
Paths = None
NerDataSet = None
PerceptronNer = None
PerceptronNerTrainer = None
AnnotationStyle = None
Files = None
trainPath = None
testPath = None
modelRoot = None
morphology = None
ner = None

def init_libs():
	global init
	global TurkishMorphology
	global Paths
	global NerDataSet
	global PerceptronNer
	global PerceptronNerTrainer
	global AnnotationStyle
	global Files
	global trainPath
	global testPath
	global modelRoot
	global morphology
	global ner

	TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
	Paths = jp.JClass('java.nio.file.Paths')
	NerDataSet = jp.JClass('zemberek.ner.NerDataSet')
	PerceptronNer = jp.JClass('zemberek.ner.PerceptronNer')
	PerceptronNerTrainer = jp.JClass('zemberek.ner.PerceptronNerTrainer')
	AnnotationStyle = jp.JClass('zemberek.ner.NerDataSet.AnnotationStyle')
	Files = jp.JClass('java.nio.file.Files')

	modelRoot = Paths.get("zemberek/data/ner/ner_created_model")
	morphology = TurkishMorphology.createWithDefaults()
	ner = PerceptronNer.loadModel(modelRoot, morphology)

def train_ner():
	global init
	global TurkishMorphology
	global Paths
	global NerDataSet
	global PerceptronNer
	global PerceptronNerTrainer
	global AnnotationStyle
	global Files
	global trainPath
	global testPath
	global modelRoot
	global morphology

	if init == False:
		# Import the required Java classes
		TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
		Paths = jp.JClass('java.nio.file.Paths')
		NerDataSet = jp.JClass('zemberek.ner.NerDataSet')
		PerceptronNer = jp.JClass('zemberek.ner.PerceptronNer')
		PerceptronNerTrainer = jp.JClass('zemberek.ner.PerceptronNerTrainer')
		AnnotationStyle = jp.JClass('zemberek.ner.NerDataSet.AnnotationStyle')
		Files = jp.JClass('java.nio.file.Files')
		init = True

	trainPath = Paths.get("zemberek/data/ner/ner_train_data.txt")
	testPath = Paths.get("zemberek/data/ner/ner_test_data.txt")
	modelRoot = Paths.get("zemberek/data/ner/ner_created_model")
	
	trainingSet = NerDataSet.load(trainPath, AnnotationStyle.ENAMEX)
	testSet = NerDataSet.load(testPath, AnnotationStyle.ENAMEX)
	morphology = TurkishMorphology.createWithDefaults()

	nerTrainer = PerceptronNerTrainer(morphology)
	ner = nerTrainer.train(trainingSet, testSet, 13, 0.1)
	Files.createDirectories(modelRoot)
	ner.saveModelAsText(modelRoot)

def ner_tagging(sentence):
	global init
	global TurkishMorphology
	global Paths
	global NerDataSet
	global PerceptronNer
	global PerceptronNerTrainer
	global AnnotationStyle
	global Files
	global trainPath
	global testPath
	global modelRoot
	global morphology
	global ner

	result = ner.findNamedEntities(sentence)
	namedEntities = result.getNamedEntities()

	for namedEntity in namedEntities:
		print(namedEntity)
