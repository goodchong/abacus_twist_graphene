export MY_CONTAINER="abacus_gpu_zhc"
num=`docker ps -a|grep "$MY_CONTAINER"|wc -l`
echo $num
echo $MY_CONTAINER
if [ 0 -eq $num ]
then
  echo "create"
    docker run \
    --gpus all \
    -it --name $MY_CONTAINER \
    --privileged \
    --net=host \
    -v `pwd`:/mnt \
    abacusdft/abacus:v3.4.0_cuda \
    /bin/bash
  else 
  echo "run"
  docker start $MY_CONTAINER
  docker exec -ti $MY_CONTAINER /bin/bash
fi
date
