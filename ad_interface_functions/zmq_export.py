import zmq


def zmq_export(sock: zmq.Socket, topic: str, data, datatype: str = "pyobj"):
    """
    Author:
    Alexander Heilmeier & Tim Stahl

    Description:
    Sends data via ZMQ.

    Inputs:
    sock:       ZMQ socket (see below how to create it)
    topic:      ZMQ topic to use
    data:       data to send
    datatype:   string that indicates if it should be sent as Python object (pyobj), json (json) or string (str)

    Hint: To send an object as string it must be converted to a string at first. Conversion of Python objects to json
    objects is handled by PyZMQ and therefore must not be done by hand if sending a json.

    How to create a ZMQ socket to export data?
    import zmq
    zmq_context = zmq.Context()
    sock = zmq_context.socket(zmq.PUB)
    sock.bind("tcp://*:%s" % port)
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
