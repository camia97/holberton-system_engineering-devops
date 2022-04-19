file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0744',
  content => 'Host * \nPasswordAuthentication no\n IdentityFile ~/.ssh/school'
}
