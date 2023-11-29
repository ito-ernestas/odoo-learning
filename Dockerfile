FROM odoo:17

USER root

# install zsh, make
RUN apt-get update && apt-get install -y zsh make

# install oh-my-zsh
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -p git -p ssh-agent -p https://github.com/zsh-users/zsh-autosuggestions -p https://github.com/zsh-users/zsh-completions

COPY .p10k.zsh /root/.p10k.zsh
COPY .zshrc /root/.zshrc

USER odoo
