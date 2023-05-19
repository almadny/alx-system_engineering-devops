# Manifest to change number of open files by a worker process
exec { 'change_open_file_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path 	  => '/usr/local/bin/:/bin/',
}

# Restart the nginx server
exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
