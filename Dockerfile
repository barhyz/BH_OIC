FROM python:3.9

RUN apt-get update
RUN apt-get install vim -y
RUN mkdir -p /home/cloud

# Run 
CMD ["/bin/bash"]

# docker run -it --name python39 –v /Users/mz/Documents/Mateusz/Work/WUT/test_cloud/:/home/cloud python39
