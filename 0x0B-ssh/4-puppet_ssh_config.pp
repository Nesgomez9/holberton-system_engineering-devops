# Puppet file that alows me to change the ssh config
file_line { 'Turn off password Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no'
}
file_line { 'Define a new identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/holberton'}