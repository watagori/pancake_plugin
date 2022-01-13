FROM python:3
USER root

RUN pip install web3
RUN pip install eth-event
RUN pip install etherscan-python
RUN pip install git+https://github.com/ca3-caaip/senkalib\#egg=senkalib -t /senkalib
RUN export PYTHONPATH="./senkalib:$PYTHONPATH"