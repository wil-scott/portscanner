import socket
import threading
import asyncio
import aiohttp
import concurrent.futures


class Scanner:
    def __init__(self):
        pass

    def scan_port(self, ip, port):
        """
        Scan a port on the machine identified by the given IP address.

        @param ip: a string representing an IP address
        @param port: an int representing a valid port number
        return: true if open else false
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = False
        try:
            sock.connect((ip, port))
            result = True
        except:
            pass
        finally:
            return result

    def scan_ports(self, ip, port_list):
        """
        Scan multiple ports via multiple threads.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.scan_port, ip, port) for port in port_list]

            for future in concurrent.futures.as_completed(futures):
                future.result()
