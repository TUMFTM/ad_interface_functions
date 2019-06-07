import socket
from typing import Union


def udp_import(sock: socket.socket, data_size: int, use_buffer: bool = False) -> Union[bytes, list]:
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    Import data via UDP. data_size in bytes! use_buffer flag can be used to return the complete buffer instead of just
    returning the latest message.
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

    if use_buffer:
        return buffer
    else:
        return data_b


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
