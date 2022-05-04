<<<<<<< HEAD
from base.controller import Controller
from algorithm.multidupehack import Multidupehack
from algorithm.triclusterbox import TriClusterBox
from algorithm.paf import Paf
from algorithm.paf_maxgrow import PafMaxGrow
from algorithm.getf import Getf
from algorithm.cancer import Cancer
from base.file_system import FileSystem

controller = Controller()
multidupehack = Multidupehack(controller)
paf = Paf(controller)
pafmaxgrow = PafMaxGrow(controller)
getf = Getf(controller)
# triclusterbox = TriClusterBox(controller)
cancer = Cancer(controller)

controller.initiateSession()
# controller.initiatePostAnalysis()
# controller.initiatePostAnalysis()
=======
from base.controller import Controller
from algorithm.multidupehack import Multidupehack
from algorithm.triclusterbox import TriClusterBox
from algorithm.paf import Paf
from algorithm.paf_maxgrow import PafMaxGrow
from algorithm.getf import Getf
from algorithm.cancer import Cancer
from base.file_system import FileSystem

controller = Controller()
multidupehack = Multidupehack(controller)
paf = Paf(controller)
pafmaxgrow = PafMaxGrow(controller)
getf = Getf(controller)
# triclusterbox = TriClusterBox(controller)
cancer = Cancer(controller)

# controller.initiateSession()
controller.initiatePostAnalysis()
controller.initiatePostAnalysis()
>>>>>>> 3a4087cc24e19cec69c8cae052603070b000c29c
