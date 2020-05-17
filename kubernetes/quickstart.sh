kind create cluster
kubectl apply -f .
PORT=3000
kubectl expose deploy paisen --port $PORT
echo "waiting for executing pods ..."
sleep 20
echo "access localhost:$PORT"
kubectl  port-forward svc/paisen $PORT

