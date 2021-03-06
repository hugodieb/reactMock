FROM python:3.6

RUN apt-get update --fix-missing && \
    apt-get install -y curl nano git locales zip unzip   

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    echo "export LS_OPTIONS='--color=auto'" >>~/.bashrc && \
    echo "eval "\`dircolors\`"" >>~/.bashrc && \
    echo "alias ls='ls \$LS_OPTIONS'" >>~/.bashrc && \
    echo "alias ll='ls \$LS_OPTIONS -l'" >>~/.bashrc && \
    echo "alias l='ls \$LS_OPTIONS -lA'" >>~/.bashrc

RUN cd /tmp && \
    wget --quiet https://nodejs.org/dist/v12.11.0/node-v12.11.0-linux-x64.tar.xz && \
    tar xf node-v12.11.0-linux-x64.tar.xz && \
    cp -r node-v12.11.0-linux-x64/* /usr && \
    rm node-v12.11.0-linux-x64.tar.xz && \
    npm install pm2 -g

WORKDIR /app

COPY frontend/package.json frontend/package.json
RUN cd frontend && npm install
COPY frontend frontend
RUN cd frontend && npm run build
COPY backend/package.json backend/package.json
RUN cd backend && npm install
COPY backend backend
RUN cd backend && npm build
ENV SHELL=/bin/bash PYTHONUNBUFFERED=1
COPY . /app
COPY docker/bin/* /usr/bin/
