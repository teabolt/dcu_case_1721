source .env.redis
source .env.postgres
source .env.postgres.user  # THIS SHOULD BE KEPT PRIVATE
source .env.postgres.password  # THIS SHOULD BE KEPT PRIVATE


kubectl create configmap redis --from-env-file=.env.redis
kubectl get configmap redis -o yaml > redis.configmap.yaml
kubectl delete configmap redis

kubectl create configmap postgres --from-env-file=.env.postgres
kubectl get configmap postgres -o yaml > postgres.configmap.yaml
kubectl delete configmap postgres

kubectl create secret generic postgres --from-literal=POSTGRES_USER=$POSTGRES_USER --from-literal=POSTGRES_PASSWORD=$POSTGRES_PASSWORD
kubectl get secret/postgres -o yaml > postgres.secret.yaml
kubectl delete secret/postgres
