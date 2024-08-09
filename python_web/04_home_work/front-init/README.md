# homework_2
1) Build image
```docker build . -t radzihowski/hw4:0.0.1```
2) Push to dockerhub
```docker push radzihowski/hw4:0.0.1```
3) Pull image to server
```docker pull radzihowski/hw4:0.0.1```
4) Run container on server
```docker run -it --name hw2oleksandr -p 3000:3000 -v .\storage:/storage radzihowski/hw4:0.0.1```