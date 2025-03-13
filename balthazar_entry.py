from laser_setup.config import config, instantiate
from laser_setup.display.app import display_window
from laser_setup.parser import experiment_list


def main():
    while (procedure := input("Procedure: ")) not in experiment_list:
        print(f"Invalid procedure: {procedure}")

    idx = experiment_list.index(procedure)
    display_window(instantiate(
        config.Qt.MainWindow.procedures[idx].target, level=1
    ))


if __name__ == '__main__':
    main()
