FROM odoo:17

USER root

RUN pip3 install debugpy

RUN apt-get update && apt-get install -y zsh make vim git wget fontconfig

RUN mkdir /odoo && chown odoo: /odoo
RUN usermod -d /odoo odoo
ENV HOME=/odoo

USER odoo
WORKDIR $HOME

COPY ./zsh/.p10k.zsh $HOME/.p10k.zsh
COPY ./zsh/.zshrc $HOME/.zshrc

RUN git clone --depth=1 https://github.com/powerline/fonts.git ${HOME}/fonts
RUN /bin/zsh -c '${HOME}/fonts/install.sh'

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -p git \
    -p ssh-agent \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions


CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "/usr/bin/odoo", "--db_host", "db", "--db_port", "5432", "--db_user", "odoo", "--db_password", "odoo"]
