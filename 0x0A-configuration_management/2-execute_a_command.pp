# Kills the killmenow process through a manifest

exec {
        'killmenow':
        command => '/usr/bin/pkill killmenow'
}
