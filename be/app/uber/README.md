# Uber-like App

## Run
### BE

1. GRPC Gateway

```
.\src\grpc-gw\grpc-gw.exe
```

2. Location App
```
.\src\server\poetry run python location_app.py --port=50051
```

3. Matching App (Not implemented yet)
```
.\src\server\poetry run python match_app.py --port=60051
```

4. LB for Location App

```
.\src\lb\docker-compose up --build -d
```



5. Random Driver Location Report
.\src\test\random_driver.py

6. Client
.\src\test\map_fe.html

![](app.JPG)