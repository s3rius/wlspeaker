import pulsectl
from loguru import logger

from wlspeaker import configure_logging


def main():
    """Start pulseaudio server."""
    configure_logging()
    tcp_module = "module-native-protocol-tcp"
    with pulsectl.Pulse("wlspeaker-server") as pulse:
        logger.info("Starting server")
        for module in pulse.module_list():
            if module.name == tcp_module:
                logger.error("TCP module already loaded. Unloading...")
                pulse.module_unload(module.index)
        logger.info("Loading server module")
        index = pulse.module_load(
            tcp_module,
            "auth-anonymous=true",
        )
        logger.info(f"Module index: {index}")
