import os
import sys

from matrix_client.api import MatrixHttpApi

homeserver = os.environ.get("INPUT_HOMESERVER", None)
token = os.environ.get("INPUT_TOKEN", None)
channel = os.environ.get("INPUT_CHANNEL", None)
message = os.environ.get("INPUT_MESSAGE", None)

if homeserver is None:
    sys.exit(1)

if token is None:
    sys.exit(1)

if channel is None:
    sys.exit(1)

if message is None:
    sys.exit(1)

matrix = MatrixHttpApi(homeserver, token=token)
matrix.send_message(channel, message)
