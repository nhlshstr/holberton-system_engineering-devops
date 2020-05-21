# Typo in wp-settings.php
exec { 'replaces typo with .php':
  command => "sed -i -e 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
