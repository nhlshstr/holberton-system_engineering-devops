# Using puppet to configure a private key, and to refuse p/w

file_line { 'No p/w authentication':
        path => '~/.ssh/config',
        line => 'KbdInteractiveAuthentication no'
}

file_line { 'Key file specification in .ssh config':
        path => '~/.ssh/config',
        line => 'IdentifyFile ~/.ssh/holberton'
}
