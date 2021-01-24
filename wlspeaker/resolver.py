import socket
from operator import attrgetter
from typing import List

from icmplib import multiping
from loguru import logger


def get_ip() -> str:
    """Determine your local IP.

    This function trying to get your ip from random socket
    connection.

    :return: IP address of this computer in local network.
    """
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_addr = "127.0.0.1"
    try:  # noqa: WPS229
        sock_client.connect(("10.255.255.255", 1))
        ip_addr = sock_client.getsockname()[0]
    except ConnectionRefusedError as exc:
        logger.error(exc)
    sock_client.close()
    return ip_addr


def scan_network(local_address: str) -> List[str]:
    """
    Get all ip addresses in network.

    Retrieve all addresses reachable by this pc.

    :param local_address: your local IP.
    :return: List of addresses strings.
    """
    base_ip, _, local_addr = local_address.rpartition(".")
    ips = []
    for addr in range(0, 254 + 1):  # noqa: WPS432
        if str(addr) != local_addr:
            ips.append(f"{base_ip}.{addr}")
    return list(
        map(
            lambda node: str(node.address),
            filter(attrgetter("is_alive"), multiping(ips, count=1, privileged=False)),
        )
    )


def find_network_neighbours() -> List[str]:
    """
    Find all wireless speakers.

    This function works as following:
        * get your ip in local network.
        * finds all other available ips in this networks.
        * pings them on specific udp port.

    :return: list of available nodes in network.
    """
    local_ip = get_ip()
    neighbours = scan_network(local_ip)
    logger.info(f"Found neighbours: {neighbours}")
    return neighbours
