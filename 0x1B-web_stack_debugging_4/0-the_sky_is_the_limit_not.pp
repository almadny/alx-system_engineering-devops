# Manifest to change number of open files by a worker process

exec {'change_open_file_limit':
        command => "sed -i 's/15/4000/' /etc/default/nginx",
	path => "/usr/local/bin/:/bin/"
}
exec {'restart_nginx':
        command => "nginx restart",
	path => "/etc/init.d/"
}
