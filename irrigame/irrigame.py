"""Main module."""
import signal
import sys

from . import config
from .sensors import TankLevel

tankLevel = None


def setup():
    print('IrrigaMe setup running...')
    # TODO: project setup
    tankLevel = TankLevel(config.TANK_LEVEL_MIN_DISTANCE, config.TANK_LEVEL_MAX_DISTANCE,
                          config.TANK_LEVEL_TRIGGER_PIN, config.TANK_LEVEL_ECHO_PIN)
    print('IrrigaMe setup finished!')


def loop():
    # TODO: project loop
    print(tankLevel.measure_one())
    pass


def teardown(sig, frame):
    print('Exiting...')
    sys.exit(1)


def main():
    signal.signal(signal.SIGINT, teardown)
    setup()
    while(True):
        loop()
