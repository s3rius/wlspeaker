"""wlspeaker.

Wireless speaker lib
====================

This module made to detect all computers in your network
and load them as pulseaudio sinks.
"""
import logging
import sys

from loguru import logger


def configure_logging():
    """Set logging basicConfig."""
    logger.remove()
    logger.add(
        sys.stderr,
        level=logging.DEBUG,
        format="<level>{level}</level>: {message}",
        colorize=True,
    )
