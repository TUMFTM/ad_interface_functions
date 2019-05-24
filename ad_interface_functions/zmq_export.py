import zmq


def zmq_export(sock: zmq.Socket, topic: str, data, datatype: str = "pyobj"):
    """
    Created by:
    Alexander Heilmeier & Tim Stahl

    Documentation:
    Sends data via ZMQ.
    """

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCTION BODY ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    sock.send_string(topic, zmq.SNDMORE)

    if datatype == "pyobj":
        sock.send_pyobj(data)
    elif datatype == "json":
        sock.send_json(data)
    elif datatype == "str":
        sock.send_string(data)
    else:
        raise ValueError("Specified datatype is not supported!")


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
