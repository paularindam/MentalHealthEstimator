from os import listdir
import pandas as pd
from pandas import DataFrame
from orderedDict import *
import os,string,sys,csv,re,pickle,requests,random, ast
from helperAlchemy import *
from autocorrect import spell
from numpy import mean, std,array, median, ptp, var, percentile,save

from langdetect import detect
import detectlanguage
from detectlanguage import simple_detect as detectLanguage
detectlanguage.configuration.api_key = "YOUR_KEY_HERE" #Email detectLanguage for your own key

def loadNumpy(name,path='.'):
    fullPath = path+'/'+name+'.npy'
    return load(fullPath)

def isEnglish(text):
    print "This work uses detectLanguage's API as one of the ingredients for classification. Email detectLanguage for your own key."
    if detectLanguage(text)=='en' and detect(text)=='en' and get_language(text)=='english' and TextBlob(text).detect_language()=='en':
        return True
    return False
