from email.mime import base
from models.experiment import Experiment
import time
from base.configs import Configs
from models.pattern import Pattern
from utils.commands import Commands
from models.experiment_cluster import ExperimentCluster
import re
class FileSystem():
    
    @staticmethod
    def createIterationFolders(iteration, configuration_name):
        tensors_folder = f"../iterations/{configuration_name}/{iteration}/tensors"
        gennsets_folder = f"../iterations/{configuration_name}/{iteration}/tensors/gennsets"
        numnoise_folder = f"../iterations/{configuration_name}/{iteration}/tensors/numnoise"
        numpy_folder = f"../iterations/{configuration_name}/{iteration}/tensors/numpy"
        mat_folder = f"../iterations/{configuration_name}/{iteration}/tensors/mat"

        folders = [tensors_folder, gennsets_folder, numnoise_folder,numpy_folder, mat_folder]
        Commands.createFolders(folders)

    @staticmethod
    def createPostAnalysisFolder(configuration_name):
        post_analysis_folder = f"../post_analysis/{configuration_name}"
        Commands.createFolder(post_analysis_folder)

    @staticmethod
    def deletePostAnalysisFolder():
        post_analysis_folder = "../post_analysis"
        Commands.deleteFolder(post_analysis_folder)

    @staticmethod
    def deleteIterationFolders():
        Commands.deleteFolder("../iterations")
    
    @staticmethod
    def createExperimentFolder(iteration, experiment, configuration_name):
        experiment_folder = f"../iterations/{configuration_name}/{iteration}/output/{experiment}/experiments"
        log_folder = f"../iterations/{configuration_name}/{iteration}/output/{experiment}/logs"

        folders = [experiment_folder, log_folder]
        Commands.createFolders(folders)

    @staticmethod
    def delete(folder):
        Commands.deleteFolder(folder)

    @staticmethod
    def getExperimentClusters(configuration_name) -> list:
        experiment_clusters = []
        iterations_folder = f"../iterations/{configuration_name}"
        for iteration in Commands.listFolder(iterations_folder):
            print(f"Getting clusters of iteration {iteration}")
            output_folder = f"{iterations_folder}/{iteration}/output"

            for cluster_folder in Commands.listFolder(output_folder):
                co = int(re.search("co(\d*)", cluster_folder)[1])
                u = float(re.search("-u(\d\.\d*)", cluster_folder)[1])
                base_folder = f"../iterations/{configuration_name}/{iteration}/output/{cluster_folder}"
                cluster = ExperimentCluster(base_folder, iteration, u, co)
                experiment_clusters.append(cluster)

        return experiment_clusters

    @staticmethod
    def getPlantedPatterns(iteration, configuration_name):
        patterns = []
        configs = Configs()
        dimension = len(configs.getParameter("dataset_size"))
        patterns_file = f"../iterations/{configuration_name}/{iteration}/tensors/gennsets/dataset.tensor"

        with open(patterns_file) as patterns:
            patterns = [Pattern(pattern, dimension) for pattern in patterns]
        
        return patterns

    @staticmethod
    def getConfigurationNames():
        configuration_names = []
        configs_folder = "configs"
        for config_file in Commands.listFolder(configs_folder):
            Configs.readConfigFile(f"{configs_folder}/{config_file}")
            configuration_names.append(Configs.getParameter("configuration_name"))

        return configuration_names

    @staticmethod
    def getDoneIterations(configuration_name):
        iterations = [int(folder) for folder in Commands.listFolder(f"../iterations/{configuration_name}")]
        return iterations

    @staticmethod
    def getClusterFoldersByU(base_folder, u):
        filtered_clusters = []
        pattern = f"co\d*-u{u}"
        for cluster_folder in Commands.listFolder(base_folder):
            if re.search(pattern, cluster_folder) is not None: # found
                filtered_clusters.append(cluster_folder)
        return filtered_clusters

    @staticmethod
    def deleteUFromAllIterations(configuration_name, u, algorithm_name):
        for iteration in FileSystem.getDoneIterations(configuration_name):
            base_folder = f"../iterations/{configuration_name}/{iteration}/output"
            cluster_folders = FileSystem.getClusterFoldersByU(base_folder, u)

            for cluster_folder in cluster_folders:
                experiment_path = f"{base_folder}/{cluster_folder}/experiments/{algorithm_name}.experiment"
                log_path = f"{base_folder}/{cluster_folder}/logs/{algorithm_name}.log"

                Commands.deleteFile(experiment_path)
                Commands.deleteFile(log_path)

    
