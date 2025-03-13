from .config import config, instantiate
from .display.app import display_window
from .parser import experiment_list


def main():
    while (procedure := input("Procedure: ")) not in experiment_list:
        print(f"Invalid procedure: {procedure}")

    idx = experiment_list.index(procedure)
    display_window(instantiate(
        config.Qt.MainWindow.procedures[idx].target, level=1
    ))


if __name__ == '__main__':
    main()
