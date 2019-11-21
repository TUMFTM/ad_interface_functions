import socket


def udp_export(sock: socket.socket, ip: str, port: int, data_b: bytes):
    """"
    Author:
    Alexander Heilmeier

    Description:
    Export data via UDP.

    Inputs:
    sock:       UDP socket (see below how to create it)
    ip:         IP address of desired receiver
    port:       port number of desired receiver
    data_b:     data to send (must be a bytes object, e.g. by using struct.pack or np.tobytes)

    How to create a UDP socket to export data?
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCTION BODY ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    sock.sendto(data_b, (ip, port))


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
