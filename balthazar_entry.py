import os

from laser_setup.config import config, instantiate
from laser_setup.display.app import display_window
from laser_setup.parser import experiment_list

import balthazar as blt


def main():
    config._session["args"] = {"debug": True}

    procedure = blt.params["Procedure type"]
    idx = experiment_list.index(procedure)
    display_window(instantiate(
        config.Qt.MainWindow.procedures[idx].target, level=1
    ))


if __name__ == '__main__':
    main()
