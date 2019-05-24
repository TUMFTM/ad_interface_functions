import zmq


def zmq_import(sock: zmq.Socket, blocking: bool = False, datatype: str = "pyobj"):
    """
    Created by:
    Alexander Heilmeier & Tim Stahl

    Documentation:
    Handles incoming ZMQ messages.
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Specify called receive handle ------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    if datatype == "pyobj":
        sock_recv_fct = lambda **kwargs: sock.recv_pyobj(**kwargs)
    elif datatype == "json":
        sock_recv_fct = lambda **kwargs: sock.recv_json(**kwargs)
    elif datatype == "str":
        sock_recv_fct = lambda **kwargs: sock.recv_string(**kwargs)
    else:
        raise ValueError("Specified datatype is not supported!")

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCTION BODY ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    data = None

    # non blocking socket to empty buffer
    try:
        while True:
            sock.recv_string(flags=zmq.NOBLOCK)
            data = sock_recv_fct(flags=zmq.NOBLOCK)
    except zmq.Again:
        pass

    # if no data was received above and blocking is True, wait for new data
    if data is None and blocking:
        sock.recv_string()
        data = sock_recv_fct()

    return data


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
