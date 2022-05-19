from numpy import True_
from base.gennsets import Gennsets
from base.numnoise import Numnoise
from base.configs import Configs
from base.numpy_translator import NumpyTranslator
from base.mat_translator import MatTranslator
from models.attribute import Attribute
from utils.commands import Commands
from post_analysis.grapher import Grapher
from base.file_system import FileSystem
from multiprocessing import Process
class Controller():
    def __init__(self) -> None:
        self.__configs_folder = "configs"
        self.algorithms = []
        self.__gennsets = Gennsets(self)
        self.__numnoise = Numnoise(self)
        self.__numpy_translator = NumpyTranslator(self)
        self.__mat_translator = MatTranslator(self)

        self.__current_iteration_number = None
        self.__current_configuration_name = None
        self.current_iteration_folder = None
        self.current_experiment = None
        self.__ufmg_mode = False

    def ufmgMode(self):
        return self.__ufmg_mode

    def addAlgorithm(self, algorithm):
        if algorithm not in self.algorithms:
            self.algorithms.append(algorithm)
    
    def __runIterations(self):
        for iteration in range(1, self.__current_iteration_number+1):
            print("@"*120 + f" ITERATION = {iteration}")
            FileSystem.createIterationFolders(iteration, self.__current_configuration_name)
            self.current_iteration_folder = f"../iterations/{self.__current_configuration_name}/{iteration}"
            self.__gennsets.run()

            for observations in Configs.getParameter("correct_obs"):
                print("#"*120 + f" CORRECT OBSEVATIONS = {observations}")
                self.__numnoise.run(observations)
                self.__numpy_translator.run(observations)
                self.__mat_translator.run(observations)

                for u in Configs.getParameter("u_values"):
                    print("="*120 + f" U VALUE = {u}")
                    self.current_experiment = f"co{observations}-u{u}"
                    FileSystem.createExperimentFolder(iteration, self.current_experiment, self.__current_configuration_name)

                    for algorithm in self.algorithms:
                        if algorithm.hasTimedOut(u):
                            continue

                        timedout = algorithm.run(u, observations, Configs.getParameter("timeout"))
                        if timedout:
                            algorithm.timedOut(u)
                            FileSystem.deleteUFromAllIterations(self.__current_configuration_name, u, algorithm.name)
                        print("-"*120)

    def __resetAlgorithms(self):
        for algorithm in self.algorithms:
            algorithm.resetTimeOutInfo()

    def initiateSession(self):
        is_on_ufmg = str(input("Is on ufmg? Y/N: ")).strip().lower()
        if is_on_ufmg == "y":
            self.__ufmg_mode = True

        delete_iterations = str(input("Delete previous iterations? Y/N: ")).strip().lower()
        if delete_iterations == "y":
            FileSystem.deleteIterationFolders()

        FileSystem.deletePostAnalysisFolder()

        for config_file in Commands.listFolder(self.__configs_folder):
            Configs.readConfigFile(f"{self.__configs_folder}/{config_file}")
            self.__current_configuration_name = Configs.getParameter("configuration_name")
            self.__current_iteration_number = Configs.getParameter("nb_iterations")
            self.__resetAlgorithms()
            self.__runIterations()
                    
    def __analyseConfiguration(self, configuration_name, save):
        FileSystem.createPostAnalysisFolder(configuration_name)
        post_analysis_folder = f"../post_analysis/{configuration_name}" 
        grapher = Grapher(configuration_name)
        print("Plotting pattern nb graph")
        grapher.setAttribute(Attribute.PATTERN_NUMBER)
        # grapher.setYLimits(0.6, 110_000)
        grapher.setYLimits(0.6, 2_000_000)
        grapher.drawGraph(post_analysis_folder, save)

        print("Plotting memory graph")
        grapher.setAttribute(Attribute.MEMORY)
        grapher.setYLimits(1e-2, 500)
        grapher.drawGraph(post_analysis_folder, save)

        print("Plotting run time graph")
        grapher.setAttribute(Attribute.RUN_TIME)
        grapher.setYLimits(1e-3, 1e3)
        grapher.drawGraph(post_analysis_folder, save)

        print("Plotting quality graph")
        grapher.setAttribute(Attribute.QUALITY)
        grapher.setYLimits(0, 1.1)
        grapher.drawGraph(post_analysis_folder, save)
        grapher.drawGraph(post_analysis_folder, save)

    def initiatePostAnalysis(self, save=True):
        print("#"*120)
        delete_analysis = str(input("Delete previous post analysis? Y/N: ")).strip().lower()
        if delete_analysis == "y":
            FileSystem.deletePostAnalysisFolder()

        for config_file in Commands.listFolder(self.__configs_folder):
            Configs.readConfigFile(f"{self.__configs_folder}/{config_file}")
            self.__current_configuration_name = Configs.getParameter("configuration_name")
            
            print(f"Initiating post analysis for {self.__current_configuration_name}...")
            self.__analyseConfiguration(self.__current_configuration_name, save=save)

    def getParameter(self, parameter):
        return Configs.getParameter(parameter)
