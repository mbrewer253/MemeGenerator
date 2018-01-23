from random import *
import time
#import os
#import image_scraper

#Select a random quote from meme library
#Search google images with quote
#
#
#
memeLib = {
    1:"Pepe",
    2:"Ugandan Knuckles",
    3:"420",
    4:"blaze it",
    5:"tide pods",
    6:"dat boi",
    7:"wot in tarnation",
    8:"nick, circa 2012",
    9:"the tin goes skrrrr",
    10:"pickle rick",
    11:"ajit pai",
    12:"confused mr krabs",
    13:"dont talk to me or my son ever again",
    14:"it is wednesday my dudes",
    15:"rawr XD",
    16:"had to do it to em",
  }


def new(meme, memeLib):
  selectedMeme  = str(meme)
  memeLib(selectedMeme)
  found = False
  
  for c in memeLib:
    print ("Searching", end="")
    for c in range(0,2):
      print (".", end="")
      time.sleep(.5)
    print (".")
    time.sleep(.5)
    
  for c in memeLib:
    if selectedMeme == memeLib[c]:
      print(">>> ", memeLib[c], " found")
      found = True
      break
  if found == False:
    print("Meme not found")
  
  #for url in search(selectedMeme, tld='com.pk', lang='es', stop=5):
  #  print(url) 
  
  
def randomMeme(memeLib):
  totalMemes=0
  for c in memeLib:
    totalMemes+=1
  
  rndint = randint(1,totalMemes)
  selectedMeme  = memeLib[rndint]
  print("Meme Selected)",rndint,":",selectedMeme)
  
  #image_scraper.scrape_images(selectedMeme)
  #for url in search(selectedMeme, tld='com.pk', lang='es', stop=5):
  #  print(url)
  
randomMeme(memeLib)
