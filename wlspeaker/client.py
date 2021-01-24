import pulsectl
from loguru import logger

from wlspeaker import configure_logging
from wlspeaker.resolver import find_network_neighbours


def main():
    """Find all available speakers and enable them."""
    configure_logging()
    neighbours_list = find_network_neighbours()
    with pulsectl.Pulse("wlspeaker-client") as pulse:
        for neighbour in neighbours_list:
            logger.info(f"Trying enable {neighbour}")
            pulse.module_load(
                "module-tunnel-sink-new",
                "channels=2 "  # noqa: WPS221
                "rate=44100 "
                f"server={neighbour} "
                f"sink_name=wl_speaker_{neighbour} "
                f"sink_properties=device.description=wl_{neighbour}",
            )
