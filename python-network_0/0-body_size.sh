<<<<<<< HEAD
#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
=======
#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
>>>>>>> 74b62a9dd10223d5d9dedc1ae1f494359bb41b9c
