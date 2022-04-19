# Client configuration file (w/ Puppet)
file { '/etc/ssh/ssh_config':
  path    => '/etc/ssh/ssh_config',
  owner   => 'root',
  group   => 'root',
  mode    => '0744',
  content => 'Host * \nPasswordAuthentication no\n IdentityFile ~/.ssh/school'
}
