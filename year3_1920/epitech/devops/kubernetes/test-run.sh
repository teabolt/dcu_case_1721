kubectl apply -f cadvisor.daemonset.yaml

kubectl apply -f postgres.secret.yaml \
               -f postgres.configmap.yaml \
               -f postgres.volume.yaml \
               -f postgres.deployment.yaml \
               -f postgres.service.yaml

kubectl apply -f redis.configmap.yaml \
               -f redis.deployment.yaml \
               -f redis.service.yaml

kubectl apply -f poll.deployment.yaml \
               -f worker.deployment.yaml \
               -f result.deployment.yaml \
               -f poll.service.yaml \
               -f result.service.yaml \
               -f poll.ingress.yaml \
               -f result.ingress.yaml

kubectl apply -f traefik.rbac.yaml \
              -f traefik.deployment.yaml \
              -f traefik.service.yaml

# Create  database  manually  after  first  deploy
# original ...
#
# echo 'CREATE  TABLE  votes (id text  PRIMARY KEY , vote  text  NOT  NULL);' \
#     | kubectl  exec -i <postgres-deployment-id> -c <postgres-container-id> -- psql -U
#         <username>

# adapted ...
#
username=orchestrator
postgres_deployment_id=`kubectl get pods -l=app=postgres -o name`
postgres_container_id="postgres"
echo 'CREATE TABLE votes (id text PRIMARY KEY, vote text NOT NULL);' \
    | kubectl exec -i $postgres_deployment_id -c $postgres_container_id -- psql -U $username
# may need to create the user db first with:
# createdb -U $username $username


# Adds 2 fake  DNS to /etc/hosts
echo "$(kubectl get nodes -o jsonpath='{ $.items[*].status.addresses [?(@.type =="ExternalIP")].address }') poll.dop.io result.dop.io" \
        | sudo  tee -a /etc/hosts


# check websites
curl result.dop.io:30021
curl poll.dop.io:30021
# curl localhost:30042 # FIXME: why localhost ??
curl poll.dop.io:30042
