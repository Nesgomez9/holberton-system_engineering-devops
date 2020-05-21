# Web stack debugging 3
exec { 'fix-wp-settings':
  command     => '/bin/sed -i "s/phpp/php/" /var/www/html/wp-settings.php'
}