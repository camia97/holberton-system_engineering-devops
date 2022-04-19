file { 'ssh_config'
  content => 'PasswordAuthentication no\n IdentityFile ~/.ssh/school'
}
