Title: Running Docker Inside Docker Container On Mac
Date: 2019-12-05
Category: tech
Tags: tech, docker, mac

I try to run everything in a docker container so my workstation doesn't get cluttered. This is very easy on Linux as I can run attached to the host network and expose the docker api over a tcp port so I can interact with the docker daemon inside the docker container. This isn't as easy on Mac because for some reason you can't expose the docker api over a tcp port. To get around this I use `socat` to create a bridge between the unix docker socket and an address of my choosing, like so

`socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock &`

which should make the api available at `localhost:2375` which is reachable inside the docker container.
