git clone https://github.com/google/cadvisor.git
kubectl apply -k cadvisor/deploy/kubernetes/base/
kubectl get daemonset cadvisor --namespace=cadvisor -o yaml > cadvisor.daemonset.yaml
