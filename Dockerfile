# Container/Image name
FROM python:3.8-slim-buster
LABEL maintainer="Ron Chang<ron.hsien.chang@gmail.com>"

# Prepare packages
ARG PRODUCT_NAME="app"
ENV ENV="/root/.bashrc"
RUN mkdir -p /${PRODUCT_NAME}
WORKDIR /${PRODUCT_NAME}

# Environment
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONIOENCODING=UTF-8
ENV LANG C.UTF-8

# Linux Packages
RUN apt update
# Generally use software
RUN apt install -y software-properties-common
RUN apt install -y cmake tzdata locales
RUN apt install -y libpq-dev python-dev

# Timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN locale-gen zh_TW zh_TW.UTF-8 zh_CN.UTF-8 en_US.UTF-8
RUN dpkg-reconfigure -f noninteractive tzdata

# Install requirement
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

# Alias
RUN echo 'alias ls="ls --color=auto"' >> /root/.bashrc
RUN echo 'alias ll="ls -alF"' >> /root/.bashrc
RUN echo 'alias la="ls -A"' >> /root/.bashrc
RUN echo 'alias l="ls -CF"' >> /root/.bashrc
RUN echo 'alias python="python3"' >> /root/.bashrc
RUN echo 'alias pip="python3 -m pip"' >> /root/.bashrc
RUN echo 'alias start="python main.py"' >> /root/.bashrc
RUN echo 'alias run="gunicorn -c wsgi.py main:app"' >> /root/.bashrc

# Exit(1) with message if there's no command override
CMD ["sh", "-c", "echo $(date +'%Y-%m-%d %T') [c] No Service! specify your COMMAND in compose file; sh"]
