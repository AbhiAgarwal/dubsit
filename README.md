Dubsit
======

About 
=====

Dubsit is a project where I try to explore some things I feel are wrong with current search methods. I believe that search through web-crawlers is not the best way to search going forward. I think that search through using APIs of different websites, and through a variety of methods would work best.

Technology Stack
=====

- Nginx
- Tornado
- MongoDB
- Auto-Deploy (GitHub & Python)

Starting Tornado
=====

- python main.py --port=8000
- python main.py --port=8001
- python main.py --port=8002
- python main.py --port=8003

Using Github Auto Deploy (Runs on port 8005)
=====

- start the server by typing “python GitAutoDeploy.py”
- to run it as a daemon add --daemon-mode

Checking Ports
=====

- netstat -nlp
- /etc/init.d/nginx reload
- /etc/init.d/nginx start

or 

- service nginx restart
