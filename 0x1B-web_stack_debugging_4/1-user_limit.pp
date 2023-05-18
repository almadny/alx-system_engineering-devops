# Puppet Manifest to increase the hard and soft file open limit for holberton user

exec {'Increase-hard':
	command => "/usr/bin/sed -i 's/5/200/g' /etc/security/limits.conf",
}

exec {'Increase-soft':
	command => "/usr/bin/sed -i 's/4/190/g' /etc/security/limits.conf",
}  
