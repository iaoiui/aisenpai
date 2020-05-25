kind create cluster
kubectl apply -f .
PORT=13333
WAITING=0
while [ $WAITING -ne 1 ]
do 
  echo "waiting for executing pods ..."
  sleep 5
  WAITING=`kubectl get po | grep -v Running | wc -l`
done
echo "access localhost:$PORT"
kubectl  port-forward svc/paisen $PORT

