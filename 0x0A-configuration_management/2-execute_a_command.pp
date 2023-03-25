#Execute a command to kill the killmenow program

exec {'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
}
