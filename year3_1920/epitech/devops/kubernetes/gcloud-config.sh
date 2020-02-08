# config kubectl access
gcloud container clusters get-credentials orchestrator-cluster-1 --zone europe-west1-b --project orchestrator-261812


# add firewall rules to allow TCP connections on certain ports
# only external ports need to be allowed?
gcloud compute firewall-rules create web --allow tcp:30021
gcloud compute firewall-rules create admin --allow tcp:30042

# note: use the following to delete firewall rules
gcloud compute firewall-rules delete RULENAME1 RULENAME2


# scale cluster to zero to temporarily disable it
gcloud container clusters resize orchestrator-cluster-1 --zone=europe-west1-b --num-nodes=0
# scale back to enable
gcloud container clusters resize orchestrator-cluster-1 --zone=europe-west1-b --num-nodes=2
