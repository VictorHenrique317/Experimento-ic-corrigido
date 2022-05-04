from base.controller import Controller
from algorithm.multidupehack import Multidupehack
from algorithm.paf import Paf
from algorithm.getf import Getf
from base.file_system import FileSystem
from post_analysis.plotting_data import PlottingData
from models.attribute import Attribute
from models.log import Log
from post_analysis.experiment_analysis import ExperimentAnalysis
from models.pattern import Pattern
from post_analysis.quality import Quality
from base.mat_translator import MatTranslator

import time
from itertools import count
from multiprocessing import Process

def forever(number):
    while True:
        print(number)

def not_forever():
    pass

print("hello world")

# p1 = Process(target=forever, args=(1,),name='Process_forever')
# p2 = Process(target=not_forever, name='Process_not_forever')
# p1.start()
# p2.start()
# p1.join(timeout=5)
# p2.join(timeout=5)
# p1.terminate()
# p2.terminate()
#
# if p1.exitcode is None:
#     print("p1 timed out")
#
# if p2.exitcode is None:
#     print("p2 timed out")

