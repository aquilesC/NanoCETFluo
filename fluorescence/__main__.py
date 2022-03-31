import sys
import time

import yaml
from PyQt5.QtWidgets import QApplication

from fluorescence.models.experiment import FluorescenceMeasurement
from fluorescence.view.digilent_window import DAQWindow
from fluorescence.view.fiber_window import FiberWindow
from fluorescence.view.microscope_window import MicroscopeWindow
from experimentor.lib.log import log_to_screen, get_logger


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'fluorescence.yml'
    logger = get_logger()
    log_to_screen(logger=logger)
    experiment = FluorescenceMeasurement()
    experiment.load_configuration(file, yaml.UnsafeLoader)
    executor = experiment.initialize()
    while executor.running():
        time.sleep(.1)

    app = QApplication([])
    microscope_window = MicroscopeWindow(experiment)
    microscope_window.show()
    fiber_window = FiberWindow(experiment)
    fiber_window.show()
    daq_window = DAQWindow(experiment)
    daq_window.show()
    sys.exit(app.exec())