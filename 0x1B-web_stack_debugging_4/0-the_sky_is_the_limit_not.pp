# Manifest to change number of open files by a worker process

exec {'change_open_file_limit':
        command => "sed -i 's/15/4096/g' /etc/default/nginx",
	path => "/usr/local/bin/:/bin/"
}
exec {'restart_nginx':
        command => "/bin/service nginx restart",
}
