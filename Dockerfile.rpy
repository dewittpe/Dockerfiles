FROM dewittpe/latex-and-r
ARG DEBIAN_FRONTEND=noninteractive
#
################################################################################
# Install additional R packages

#RUN R -e "remotes::install_cran('keras')"
RUN R -e "remotes::install_github('rstudio/keras')"

################################################################################
# Install and set up Anaconda

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/
#RUN echo `pwd`

# Anaconda installing
RUN wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
RUN bash Anaconda3-2019.10-Linux-x86_64.sh -b
RUN /bin/rm -f Anaconda3-2019.10-Linux-x86_64.sh

# Set path to conda
ENV PATH /home/ubuntu/anaconda3/bin:$PATH

# Updating Anaconda packages
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

# install tensor flow
RUN conda create -n tf tensorflow

