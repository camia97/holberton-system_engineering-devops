# Client configuration file (w/ Puppet)
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0744',
  content => 'Host * \n PasswordAuthentication no\n IdentityFile ~/.ssh/school'
}
