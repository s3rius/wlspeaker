|py_versions| |build_statuses| |pypi_versions|

.. |py_versions| image:: https://img.shields.io/pypi/pyversions/wlspeaker?style=flat-square
    :alt: python versions

.. |build_statuses| image:: https://img.shields.io/github/workflow/status/s3rius/wlspeaker/Release%20wlspeaker?style=flat-square
    :alt: build status

.. |pypi_versions| image:: https://img.shields.io/pypi/v/wlspeaker?style=flat-square
    :alt: pypi version
    :target: https://pypi.org/project/prettyfi/


Wlspeaker lib
=============

This library helps you to connect pulseaudio on your pc's in local network.

Requirements
------------
Pulseaudio. (Tested on version 14.0)

usage
*****

Start the server:
.. code:: bash

    wls_server

On the client machine run:
.. code:: bash

    wls_client

It will discover all available speakers.
After your speakers are discovered choose one
in pavucontrol's tab that called "Output devices"
