# import RAKE
# import operator

# @inproceedings{rehurek_lrec,
#       title = {{Software Framework for Topic Modelling with Large Corpora}},
#       author = {Radim {\v R}eh{\r u}{\v r}ek and Petr Sojka},
#       booktitle = {{Proceedings of the LREC 2010 Workshop on New
#            Challenges for NLP Frameworks}},
#       pages = {45--50},
#       year = 2010,
#       month = May,
#       day = 22,
#       publisher = {ELRA},
#       address = {Valletta, Malta},
#       language={English}
# }

import json
from gensim.summarization import keywords

def keywordGen(f):

    # with open('game.json') as f:
    rawText = json.load(f)

    jsonString = json.dumps(rawText)

    print(keywords(jsonString))

# stop_dir = "SmartStoplist.txt"
# rake_object = RAKE.Rake(stop_dir)

# def Sort_Tuple(tup):

#     tup.sort(key = lambda x: x[1])
#     return tup

# keywords = Sort_Tuple(rake_object.run(jsonString))[-15:]
# print( "Keywords: ", keywords)