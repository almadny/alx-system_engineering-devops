# Manifest to change number of open files by a worker process

exec {'change_open_file_limit':
        command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx",
}
exec {'restart_nginx':
        command => "/usr/sbin/service nginx restart"
}
