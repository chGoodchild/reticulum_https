## Build example

```bash
$ mkdir -p 24.04
$ ./generate.sh
$ sudo docker build -t chGoodchild/reticulum_https:24.04 -f ./24.04/Dockerfile .
$ sudo docker run -d -p 2222:22 --name [CONTAINER_NAME] chGoodchild/reticulum_https:24.04
$ ssh -v -i ~/.ssh/id_rsa -p 2222 root@[VPS_IP_ADDRESS]
```

