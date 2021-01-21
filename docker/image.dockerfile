# This file tells docker what image must be created
# in order to be ahble to test this library
FROM ubuntu:18.04


ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV UBUNTU_RELEASE=bionic


RUN apt-get update

# Install packages
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -o Dpkg::Options::="--force-confnew" \
                    python3-pip git iputils-ping net-tools netcat screen build-essential lsb-release gnupg2 curl
RUN pip3 install setuptools
RUN pip3 install matplotlib scipy quadpy numpy
RUN echo "deb [arch=amd64] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg" | tee /etc/apt/sources.list.d/robotpkg.list
RUN curl http://robotpkg.openrobots.org/packages/debian/robotpkg.key | apt-key add -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -o Dpkg::Options::="--force-confnew" \
                    robotpkg-py36-pinocchio

# user handling
ARG myuser
ARG myuid
ARG mygroup
ARG mygid
ARG scriptdir
RUN addgroup --force-badname --gid ${mygid} ${mygroup}
RUN adduser --force-badname --gecos "" --disabled-password  --uid ${myuid} --gid ${mygid} ${myuser}
#add user to sudoers
RUN echo "${myuser} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN echo "export PATH=/opt/openrobots/bin:$PATH" >> /etc/bash.bashrc
RUN echo "export PKG_CONFIG_PATH=/opt/openrobots/lib/pkgconfig:$PKG_CONFIG_PATH" >> /etc/bash.bashrc
RUN echo "export LD_LIBRARY_PATH=/opt/openrobots/lib:$LD_LIBRARY_PATH" >> /etc/bash.bashrc
RUN echo "export PYTHONPATH=/opt/openrobots/lib/python3.6/site-packages:$PYTHONPATH" >> /etc/bash.bashrc
RUN echo "export CMAKE_PREFIX_PATH=/opt/openrobots:$CMAKE_PREFIX_PATH" >> /etc/bash.bashrc
RUN mkdir /pinocchio
RUN chmod 777 /pinocchio
