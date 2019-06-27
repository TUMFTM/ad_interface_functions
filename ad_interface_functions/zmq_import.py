import zmq


def zmq_import(sock: zmq.Socket, blocking: bool = False, datatype: str = "pyobj"):
    """
    Created by:
    Alexander Heilmeier & Tim Stahl

    Documentation:
    Handles incoming ZMQ messages.

    Inputs:
    sock:       ZMQ socket (see below how to create it)
    blocking:   set if socket should be blocking (i.e. wait until new message is received) or not
    datatype:   string that indicates if it should be received as Python object (pyobj), json (json) or string (str)

    Hint: Conversion of json objects to their original data type is handled by PyZMQ and therefore must not be done by
    hand.

    How to create a ZMQ socket to import data?
    import zmq
    zmq_context = zmq.Context()
    sock = zmq_context.socket(zmq.PUB)
    sock.connect("tcp://%s:%s" % (ip, port))
    sock.setsockopt_string(zmq.SUBSCRIBE, zmq_topic])
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
