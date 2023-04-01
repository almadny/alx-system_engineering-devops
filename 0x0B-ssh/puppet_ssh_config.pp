#Update configuration file to disable password auth and chnge id file

file { 'ssh_autoconfig':
  ensure => 'file',
}
file_line {'Turn off passwd auth':
  path    => 'ssh_autoconfig',
  line    => 'PasswordAuthentication no',
  require => File['ssh_autoconfig'],
}
file_line {'Declare identity file':
  path    => 'ssh_autoconfig',
  line    => 'IdentityFile ~/.ssh/school',
  require => File ['ssh_autoconfig'],
}
