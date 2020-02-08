#
# delete running resources (clear current state)
#

kubectl delete deployments --all
kubectl delete services --all

kubectl delete service traefik-ingress-service --namespace=kube-public
kubectl delete deployment,serviceaccount,clusterrole,clusterrolebinding traefik-ingress-controller --namespace=kube-public
kubectl delete ingresses --all

kubectl delete configmaps --all
kubectl delete secrets --all

kubectl delete persistentvolumes --all
kubectl delete persistentvolumeclaims --all
kubectl delete storageclasses manual

kubectl delete namespace cadvisor
