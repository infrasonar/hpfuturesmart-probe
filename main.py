from libprobe.probe import Probe
from lib.check.device import CheckDevice
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckDevice,
    )

    probe = Probe("hpfuturesmart", version, checks)

    probe.start()
