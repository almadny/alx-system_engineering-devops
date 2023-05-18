# Increase the server response limits
exec {'Increase-server-response-limits':
	command => "/usr/bin/sed -i 's/15/2000/g' /etc/default/nginx",
}

exec { 'nginx-restart':
  command     => '/usr/sbin/service nginx restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin',
} 
