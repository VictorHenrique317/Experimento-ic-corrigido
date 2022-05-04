from models.log import Log
from models.pattern import Pattern
class Experiment():
    def __init__(self, experiment_path, iteration, correct_observations, u, dimension) -> None:
        self.__path:str = experiment_path
        self.__patterns = []
        self.__log = None
        self.__algorithm = None
        self.__iteration = iteration
        self.__correct_observations = correct_observations
        self.__u = u
        self.__dimension = dimension
        self.__initialize()

    def __initialize(self):
        with open(self.__path) as experiment_file:
            for pattern in experiment_file:
                self.__patterns.append(Pattern(pattern, self.__dimension))

        algorithm = self.__path.split("/")[-1].split(".")[0]
        self.__algorithm = algorithm

        log_name = f"{algorithm}.log"
        log_path = self.__path.replace(f"/experiments/{algorithm}.experiment", "")
        log_path = f"{log_path}/logs/{log_name}"
        self.__log = Log(log_path)

    def getPatterns(self):
        return self.__patterns

    def getLog(self):
        return self.__log

    def getIteration(self):
        return self.__iteration

    def getCorrectObservations(self):
        return self.__correct_observations

    def getU(self):
        return self.__u
    
    def getAlgorithm(self):
        return self.__algorithm
