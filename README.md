# MySQL Container and Python

If you going to start a Mysql Docker Container, please go to the Container folder 

## RUN 

```bash
sudo  docker run -d -p 3306:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=123 my-mysql
sudo docker exec -it my-mysql bash
```


