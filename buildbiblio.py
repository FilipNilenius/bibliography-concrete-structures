# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:04:04 2013

@author: v03nifi
"""

import os
import sys
from glob import glob

# remove all pdf-files
for f in glob ('*.pdf'):    
    os.unlink (f)

# setup typeface names and their corresponding LaTeX syntax
typeFaceName = ('computermodern','times','ebgaramond','palatino')
typeFaceSyntax = (' ','\usepackage{mathptmx}','\usepackage{ebgaramond}','\usepackage[sc]{mathpazo}')


# for all typefaces
for i in range(0,len(typeFaceName)):
    texFileName = 'biblio'
    temptexFileName = 'biblio_tmp'
    sourceFile = open(texFileName+'.tex', 'r')
    tempFile   = open(temptexFileName+'.tex', 'w')
    for line in sourceFile:
        tempFile.write(line.replace('%%stringtoberemovedbypython',typeFaceSyntax[i]))
    tempFile.close()
    sourceFile.close()
    
    # build bibliography PDF file using pdflatex and biber
    os.system('pdflatex '+ temptexFileName)
    if i ==0: # only nessecary for first compilation
        print i
        os.system('biber '+ temptexFileName)
        os.system('pdflatex '+ temptexFileName)
        os.system('pdflatex '+ temptexFileName)
    
    # rename built pdf according to its typeface
    os.rename(temptexFileName+'.pdf',texFileName+'_'+typeFaceName[i]+'.pdf')
    os.remove(temptexFileName+'.tex')


# clean up auxiliary files
os.remove(temptexFileName+'.bcf')
os.remove(temptexFileName+'.aux')
os.remove(temptexFileName+'.log')
os.remove(temptexFileName+'.out')
os.remove(temptexFileName+'.run.xml')
os.remove(temptexFileName+'.bbl')
os.remove(temptexFileName+'.blg')

# make zip file
# os.system('zip bibliography_ConcreteStructures.zip *.*')