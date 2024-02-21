 #!/bin/bash

showuptime(){
: <<'COMMENT'
multiline commenting.
uptime displays total time machine has been up and running.
-p get to output in pretty format
cut -c4- gets to cut everything before the fourth character including whitespaces
COMMENT
        up=$(uptime -p | cut -c4-)
        since=$(uptime -s)
cat << EOF
-----
This machine has been up for ${up}
It has been running since ${since}
_____
EOF
}
showuptime
