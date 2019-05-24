import socket


def udp_import(sock: socket.socket, data_size: int) -> bytes:
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    Import data via UDP. data_size in bytes!
    """

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCTION BODY ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    data_b = None

    try:
        while True:
            data_b, addr = sock.recvfrom(data_size)

    except socket.error:
        pass

    return data_b


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
