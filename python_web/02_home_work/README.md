# homework_2
1) Build image
```docker build . -t radzihowski/hw2:0.0.6```
2) Push to dockerhub
```docker push radzihowski/hw2:0.0.6```
3) Pull image to server
```docker pull radzihowski/hw2:0.0.6```
4) Run container on server
```docker run -it --name hw2oleksandr -v /root/data:/app/data radzihowski/hw2:0.0.6```