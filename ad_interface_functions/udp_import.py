import socket
from typing import Union


def udp_import(sock: socket.socket, data_size: int, use_buffer: bool = False) -> Union[bytes, list, None]:
    """
    Author:
    Alexander Heilmeier

    Description:
    Import data via UDP.

    Inputs:
    sock:           UDP socket (see below how to create it)
    data_size:      data size per message in byte (not bit!)
    use_buffer:     flag to show if the buffer should be returned completely (True) or only the newest message (False)

    How to create a UDP socket to import data?
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((own_external_ip, listening_port))
    sock.setblocking(False)
    """

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCTION BODY ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    data_b = None
    buffer = []

    try:
        while True:
            data_b, addr = sock.recvfrom(data_size)

            if use_buffer:
                buffer.append(data_b)

    except socket.error:
        pass

    if use_buffer and buffer:
        return buffer
    elif use_buffer:
        return None
    else:
        return data_b


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
