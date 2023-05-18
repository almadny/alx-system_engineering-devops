# Puppet Manifest to increase the hard and soft file open limit for holberton user

exec {'Increase-hard':
	command => "/bin/sed -i 's/5/200/' /etc/security/limits.conf",
}

exec {'Increase-soft':
	command => "/bin/sed -i 's/4/190/' /etc/security/limits.conf",
}  
