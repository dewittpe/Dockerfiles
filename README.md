Dockerfiles
===========

A collection of Dockerfiles and other Docker related notes I have found to be
useful.

## Dockerfiles

### Dockerfile.latex-and-r

The purpose of this image is to have an Unbuntu based image with LaTeX, R, and
most of the packages I use on a regular basis.

### Dockerfile.rpy

R and python.  This image is expected to be useful for for cpu based work in R
and python, including Tensorflow via keras.

## Notes

### Build an image

```bash
docker build -t [imagename:tag] -f [Dockerfile] .
```

### Images

```bash
# list images
docker image ls

# delete a specific image
docker image rm [imagename]

# delete all existing images
docker image rm $(docker images -a -q)
```

### Containters

```bash
# list all existing containers
docker ps -a

# stop a specific container
docker stop [containername]

# stop all running containers
docker stop $(docker ps -a -q)

# delete a specific contain (container must be stopped first)
docker rm [containername]

# delete all stopped containers
docker rm $(docker ps -a -q)

# display logs of a container
docker logs [containername]
```

