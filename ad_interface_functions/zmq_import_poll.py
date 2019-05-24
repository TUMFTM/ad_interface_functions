import zmq


def zmq_import_poll(sock: zmq.Socket, timeout: float):
    """
    Created by:
    Alexander Heilmeier

    Documentation: Receives pyobj data via ZMQ and allows polling.
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
