project('eta-shutdown')

subdir('po')
# install sources
install_subdir('src', install_dir : '/usr/share/eta/eta-shutdown')
install_subdir('ui', install_dir : '/usr/share/eta/eta-shutdown')
install_data('data/eta-shutdown.systemd', install_dir : '/lib/systemd/system/',rename: 'eta-shutdown.service')
install_data('data/tr.org.pardus.eta.shutdown.desktop', install_dir : '/usr/share/applications/')
install_data('data/tr.org.pardus.eta.shutdown.policy', install_dir : '/usr/share/polkit-1/actions/')
