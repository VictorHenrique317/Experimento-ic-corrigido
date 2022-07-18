from base.controller import Controller
from algorithm.multidupehack import Multidupehack
from algorithm.nclusterbox import NClusterBox
from algorithm.feeded_nclusterbox import FeededNClusterBox
from algorithm.paf import Paf
from algorithm.paf_maxgrow import PafMaxGrow
from algorithm.getf import Getf
from algorithm.cancer import Cancer
from base.file_system import FileSystem
from utils.commands import Commands

controller = Controller()
cancer = Cancer(controller)
multidupehack = Multidupehack(controller)
paf = Paf(controller)
pafmaxgrow = PafMaxGrow(controller)
getf = Getf(controller)
nclusterbox = NClusterBox(controller)
#feeded_nclusterbox = FeededNClusterBox(controller)


#controller.initiateSession()
controller.initiatePostAnalysis()
# controller.initiatePostAnalysis()

