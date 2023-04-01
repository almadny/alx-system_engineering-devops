#Creates a file

file { 'school':
  ensure  => 'present',
  path    => '/home/vagrant/alx-system_engineering-devops/0x0A-configuration_management/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
