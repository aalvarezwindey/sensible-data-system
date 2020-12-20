FROM python:3.8
COPY digital_signer /
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod 777 /signer && \
    chmod 777 /generate_keys.sh
ENTRYPOINT ["/bin/bash"]