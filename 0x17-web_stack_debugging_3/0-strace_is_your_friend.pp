exec { 'Fix Wordpress':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
