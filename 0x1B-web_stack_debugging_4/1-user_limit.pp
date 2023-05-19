# Puppet Manifest to increase the file open limit for holberton user

exec { 'increase-hard-limit':
  command => '/bin/sed -i "s/5/200/" /etc/security/limits.conf',
}

exec { 'increase-soft-limit':
  command => '/bin/sed -i "s/4/190/" /etc/security/limits.conf',
}  
