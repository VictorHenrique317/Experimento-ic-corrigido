from numpy import average
from models.attribute import Attribute
from models.experiment_cluster import AveragedExperimentCluster
from base.file_system import FileSystem
import collections
class PlottingData():
    def __init__(self, configuration_name) -> None:
        self.__configuration_name = configuration_name
        self.__u = None
        self.__algorithm = None
        self.__attribute = None

        self.__original_clusters = None
        self.__initialize()
    
    def __initialize(self):
        print("Creating plotting data")
        clusters = FileSystem.getExperimentClusters(self.__configuration_name)
        self.__original_clusters = self.__averageClusters(clusters)

    def setU(self, u):
        self.__u = u

    def setAttribute(self, attribute: Attribute):
        self.__attribute = attribute

    def setAlgorithm(self, algorithm):
        self.__algorithm = algorithm

    def getXY(self):
        if self.__u is None or self.__attribute is None or self.__algorithm is None:
            print("Set u, attribute and algorithm first")
            return
        
        filtered_clusters = self.__filterClustersByU(self.__original_clusters, self.__u)
        # print(self.__original_clusters[0].getLogs())
        filtered_logs = self.__filterLogsByAlgorithm(filtered_clusters, self.__algorithm)
        attribute_values = self.__filterLogsByAttribute(filtered_logs, self.__attribute)

        self.__u = None
        self.__attribute = None
        self.__algorithm = None

        attribute_values = collections.OrderedDict(sorted(attribute_values.items()))
        xy =  (attribute_values.keys(), attribute_values.values())
        return xy
        
    def __filterClustersByU(self, clusters, u):
        return [cluster for cluster in clusters if cluster.getU() == u]

    def __filterLogsByAlgorithm(self, filtered_clusters, algorithm):
        filtered_logs = dict() #{co: log, co: log}
        for cluster in filtered_clusters:
            logs = cluster.getLogs()
            for log in logs:
                if log.getAlgorithm().lower() != algorithm.lower().replace(" ", ""):
                    continue

                filtered_logs[cluster.getCorrectObservations()] = log

        return filtered_logs

    def __filterLogsByAttribute(self, filtered_logs, attribute):
        attribute_values = dict()
        for correct_observation, log in filtered_logs.items():
            attribute_values[correct_observation] = log.getAttributeValue(attribute)

        return attribute_values
        

    def __averageClusters(self, clusters):
        print(f"Averaging {len(clusters)} clusters")
        return AveragedExperimentCluster.average(clusters)

            
        

            