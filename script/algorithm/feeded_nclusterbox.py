from algorithm.algorithm import Algorithm
from base.controller import Controller
import time
from utils.commands import Commands


class FeededNClusterBox(Algorithm):
    def __init__(self, controller:Controller) -> None:
        super().__init__()
        self.name = "feedednclusterbox"
        self.__controller = controller
        self.__controller.addAlgorithm(self)

    def __writeLog(self, elapsed_time):
        # nb_patterns = None
        # with open(self.experiment_path) as file:
        #     nb_patterns = sum([1 for line in file])
        #
        # with open(self.log_path, "a") as file:
        #     file.write(f"Run time: {elapsed_time}\n")
        #     file.write(f"Nb of patterns: {nb_patterns}")
        pass

    def run(self, u, observations, timeout):
        current_experiment = self.__controller.current_experiment
        current_iteration_folder = self.__controller.current_iteration_folder

        self.experiment_path = f"{current_iteration_folder}/output/{current_experiment}/experiments/feedednclusterbox.experiment"
        self.log_path = f"{current_iteration_folder}/output/{current_experiment}/logs/feedednclusterbox.log"
        fuzzy_tensor_path = f"{current_iteration_folder}/tensors/numnoise/dataset-co{observations}.fuzzy_tensor"
        multidupehack_path = f"{current_iteration_folder}/output/{current_experiment}/experiments/multidupehack.experiment"

        if Commands.fileExists(multidupehack_path) is False:
            print("WARNING: Multidupehack file does not exist, skipping nclusterbox multidupehack...")
            return True

        command = f"/usr/bin/time -o {self.log_path} -f 'Memory (kb): %M' "
        command += f"cat {multidupehack_path} | "
        command += f"nclusterbox -f {fuzzy_tensor_path} --ni --ns -o {self.experiment_path}"
        command += f">> {self.log_path}"

        print(command)
        start = time.time()
        timedout = Commands.executeWithTimeout(command, timeout)
        end = time.time()
        elapsed_time = end - start

        if timedout is False:
            # self.__writeLog(elapsed_time)
            pass

        return timedout