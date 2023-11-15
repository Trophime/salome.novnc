# Running docker

Start docker image:

'''bash
docker run -it --rm -p 8080:8080 trophime/salome:9.11.0-novnc
'''

Then 

'''bash
firefox --private-windows hhtp://localhost:808/vnc.html
'''

# Reference

main settings from [docker-novnc](https://github.com/theasp/docker-novnc)