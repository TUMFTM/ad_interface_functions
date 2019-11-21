import zmq


def zmq_import_poll(sock: zmq.Socket, timeout: float):
    """
    Author:
    Alexander Heilmeier

    Description:
    Handles incoming ZMQ messages and allows polling.

    Inputs:
    sock:       ZMQ socket (see below how to create it)
    timeout:    [s] timeout for polling

    How to create a ZMQ socket to import data?
    import zmq
    zmq_context = zmq.Context()
    sock = zmq_context.socket(zmq.PUB)
    sock.connect("tcp://%s:%s" % (ip, port))
    sock.setsockopt_string(zmq.SUBSCRIBE, zmq_topic])
    """

    # ------------------------------------------------------------------------------------------------------------------
    # PREPARATION ----------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # timeout conversion s -> ms
    timeout *= 1000.0

    # set standard return
    data = None

    # ------------------------------------------------------------------------------------------------------------------
    # CHECK IF BUFFER ALREADY STORES VALUES ----------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # non blocking socket to empty buffer
    try:
        while True:
            sock.recv_string(flags=zmq.NOBLOCK)
            data = sock.recv_pyobj(flags=zmq.NOBLOCK)
    except zmq.Again:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # WAIT FOR A SHORT TIME IF NO DATA WAS STORED IN THE BUFFER --------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    if data is None:
        # use poll to be able to set a timeout -> will return 1 if an event occurs, otherwise 0
        events = sock.poll(timeout=timeout)

        if events:
            # non blocking socket to empty buffer
            try:
                while True:
                    sock.recv_string(flags=zmq.NOBLOCK)
                    data = sock.recv_pyobj(flags=zmq.NOBLOCK)
            except zmq.Again:
                pass

    return data


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
