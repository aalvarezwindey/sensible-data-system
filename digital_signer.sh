
docker build -f ./digital_signer/Dockerfile -t "digital_signer:latest" .
docker run \
  --volume ${PWD}/digital_signer/keys:/keys \
  --volume ${PWD}/digital_signer/output:/output \
  -it digital_signer
