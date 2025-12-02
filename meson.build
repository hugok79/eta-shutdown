project('eta-shutdown')

subdir('po')
# install sources
install_subdir('src', install_dir : '/usr/share/eta/eta-shutdown')
install_subdir('ui', install_dir : '/usr/share/eta/eta-shutdown')
install_data('data/eta-shutdown.systemd', install_dir : '/lib/systemd/system/',rename: 'eta-shutdown.service')
