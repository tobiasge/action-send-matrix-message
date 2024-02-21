FROM python:3.11-alpine

RUN pip install matrix_client

COPY entrypoint.sh /entrypoint.sh
COPY send_message.py /send_message.py
RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]