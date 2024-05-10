## Build example

```bash
$ mkdir -p 24.04
$ ./generate.sh
$ sudo docker build -t chGoodchild/ubuntu-sshd:24.04 -f ./24.04/Dockerfile .
$ ssh -p 2222 root@[VPS_IP_ADDRESS]
$ ./generate.sh 
$ sudo docker run -d -p 2222:22 --name [CONTAINER_NAME] chGoodchild/ubuntu-sshd:24.04
$ docker exec -ti [CONTAINER_NAME] passwd
$ docker cp authorized_keys [CONTAINER_NAME]:/root/.ssh/authorized_keys
$ docker exec [CONTAINER_NAME] chown root:root /root/.ssh/authorized_keys
$ docker exec [CONTAINER_NAME] chmod 600 /root/.ssh/authorized_keys
$ docker exec [CONTAINER_NAME] passwd -d root
$ ssh -v -i ~/.ssh/id_rsa -p 2222 root@[VPS_IP_ADDRESS]
```

