# Description
This repository provides some interface functions we frequently use in our trajectory planning software stack at FTM/TUM.
Next to the simple UDP interface we also use ZeroMQ (http://zeromq.org/) and its Python bindings PyZMQ.

# List of components
* `udp_export`: UDP export function.
* `udp_import`: UDP import function.
* `zmq_export`: ZMQ export function handling pyobj, json, str.
* `zmq_import`: ZMQ import function handling pyobj, json, str.
* `zmq_import_poll`: ZMQ import function handling pyobj with polling option.

Contact persons: [Alexander Heilmeier](mailto:alexander.heilmeier@tum.de), [Tim Stahl](mailto:stahl@ftm.mw.tum.de).
