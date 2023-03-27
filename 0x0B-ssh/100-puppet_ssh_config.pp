#Update configuration file to disable password auth and chnge id file

file { '/etc/ssh/ssh_config':
  ensure => 'file',
}
file_line {'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  require => File['/etc/ssh/ssh_config'],
}
file_line {'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  require => File ['/etc/ssh/ssh_config'],
}
