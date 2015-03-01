#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
"""
import operator
import sys
import re
import codecs

def getSyllablePron(syllable):
    pron = u""
    hasVowel1 = False
    hasVowel2 = False
    hasVowel3 = False
    
    if u"a" in syllable or u"ă" in syllable or u"î"  in syllable or u"â" in syllable:
        hasVowel1 = True
    if u"e" in syllable or u"o" in syllable or u"u" in syllable:
        hasVowel2 = True
    
    for i in range(len(syllable)):
        # Consonants
        if syllable[i] == u"c":
            if (i < len(syllable) - 1) and (syllable[i+1] in [u"e", u"i"]):
                pron += u"ʧ"
            else:
                pron += u"k"
        elif syllable[i] == u"g":
            if (i < len(syllable) - 1) and (syllable[i+1] in [u"e", u"i"]):
                pron += u"ʤ"
            else:
                pron += u"g"
        elif syllable[i] == u"h":
            if (i == 0) or ((i > 0) and (i < len(syllable) - 1) and (syllable[i-1] not in [u"c", u"g"] and syllable[i+1] not in [u"e", u"i"])):
                pron += u"h"
        elif syllable[i] == u"j":
                pron += u"ʒ"
        elif syllable[i] == u"q":
                pron += u"k"
        elif syllable[i] == u"ș":
                pron += u"ʃ"
        elif syllable[i] == u"ț":
                pron += u"ʦ"
        elif syllable[i] == u"x":
                pron += u"ks"
        elif syllable[i] == u"y":
                pron += u"j"
        # Vowels
        elif syllable[i] == u"ă":
            pron += u"ə"
        elif syllable[i] == u"â" or syllable[i] == u"î":
            pron += u"ɨ"
        elif syllable[i] == u"e" and hasVowel1 == True:
            pron += u"e̯"
        elif syllable[i] == u"o" and hasVowel1 == True:
            pron += u"o̯"
        elif syllable[i] == u"u" and (hasVowel1 == True or u"e" in syllable or u"o" in syllable):
            pron += u"w"
        elif syllable[i] == u"i":
            if (hasVowel1 == True or hasVowel2 == True or hasVowel3 == True):
                if (i == len(syllable) - 1 and syllable[i-1] in u"bcdfghjklmnprsștțvxz" ):
                    pron += u"ʲ"
                else:
                    pron += u"j"
            else:
                pron += u"i"
                hasVowel3 = True
        else:
            pron += syllable[i]
    
    return pron
    
def getPronunciationFromSyllables(syllables, word):   
    pron = u""
    accent = syllables.split("'")
    if accent[0] == u"":
        accent.pop(0)
    second = accent[0].split(".")
    
    w = 0
    for length in second:
        syllable = word[w:w+int(length)]
        pron += getSyllablePron(syllable) + u"."
        w += int(length)
        
    if len(second) == 1:
        pron = pron[1:]
    return pron[:-1]

def getPronunciation(syllables):
    sil = syllables.split(".")
    syllables = ""
    word = ""
    for s in sil:
        syllables += str(len(s)) + "."   
        word += str(s)
        
    if u"xa" in syllables[1:] or u"xă" in syllables[1:] or u"xâ" in syllables[1:] or u"xe" in syllables[1:] or u"xi" in syllables[1:] or u"xo" in syllables[1:] or u"xu" in syllables[1:]:
        return u""
       
    pron = getPronunciationFromSyllables(syllables[:-1], word)

    return addStress(pron)
        
def addStress(pron):
    if '.' not in pron:
        # just 1 syllable, no stress
        return pron
    if pron[-6:] in [u"ə.ʦi.e"] or pron[-6:] in [u".bi.lə", u".ʤi.kə", u".fi.kə", u".ni.kə", u".ti.kə"] or pron[-5:] in [u".ni.e"]:
        # stress on antepenultimate syllable
        if pron.count('.') < 3:
            # max 3 syllables, first is stressed
            return "'" + pron
        else:
            # more than 3 syllables, antepenultimate is stressed
            return pron[0:pron.rfind('.', 0, pron.rfind('.', 0, pron.rfind('.') -1)-1)] + "'" + pron[pron.rfind('.', 0, pron.rfind('.', 0, pron.rfind('.') -1)-1) + 1:]
    elif pron[-1] in [u"ə", u"e"] or pron[-3:] in [u"bil", u"ʤik", u"fik", u"nik", u"tik", u"tru"]:
        # stress on penultimate syllable
        if pron.count('.') < 2:
            # just 2 syllables, first is stressed
            return "'" + pron
        else:
            # more than 2 syllables, penultimate is stressed
            return pron[0:pron.rfind('.', 0, pron.rfind('.') -1)] + "'" + pron[pron.rfind('.', 0, pron.rfind('.') -1) + 1:]
    else:
        return pron[0:pron.rfind('.')] + "'" + pron[pron.rfind(".") + 1:]

    #unknown case, do manually
    return pron
            
try:
    word = sys.argv[1]
    
    pron = getPronunciation(word)
    print pron.encode('utf-8')
        
finally:
    sys.exit(0)