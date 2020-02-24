# Advanced Scheduling Kubernetes sp20-516-232, Singam, Ashok


:o2: markdown dows not allo the use of none so we can not include it in the chapters
        
Advanced Scheduling fetatures makes Kubernetes a very flexible,policy-rich, topology-aware, workload-specific scheduler. These features provide a wide range of options to specify conditions for assigning pods to particular worker nodes that satisfy a condition. With advanced Scheduling features one can influence where pods can be scheduled among availalbe Nodes. In Kubernetes 1.6 four advanced scheduling features are added [@KubeAdvShedule-sp20-516-232]. Scope of this chapter is limited to first two features . 

1. Node affinity
2. Taints and tolerations, 
3. Pod affinity/anti-affinity 
4. Custom schedulers. 

## Node affinity to attract pods  

Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. The rules are defined using custom labels on nodes and label selectors specified in pods. Node affinity allows a pod to specify an affinity (or anti-affinity) towards a group of nodes it can be placed on. The node does not have control over the placement [@KubeImplAdvShedule-sp20-516-232]. 

For example, you could configure a pod to only run on a node with a specific CPU or in a specific availability zone. There are two types of node affinity rules: 

* Required 
* preferred

Required rules must be met before a pod can be scheduled on a node. Preferred rules specify that, if the rule is met, the scheduler tries to enforce the rules, but does not guarantee enforcement.

### Node affinity example

Print list of the nodes

```
NAME    STATUS    ROLES     AGE       VERSION
node1   Ready     *none*    5m        v1.9.4
node2   Ready     *none*    5m        v1.9.4
```

Now label node1 as Size:M1

```bash
$ kubectl label nodes node1 node1=Size:M1
```

Now for an app called Busybox, configure NodeAffinity in deployment yaml file to refer node1 label:

```
affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: "node1"
                operator: In
                values: ["Size:M1"]
```

Deploy 4 replicas of image Busybox

```bash
$ kubectl run  test-affinity --image busybox --replicas 4 -- sleep 99
```

We can observe that all the pods are scheduled on node1. No pod is scheduled on node2!

```
$ kubectl get po -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP          NODE    NOMINATED NODE   READINESS GATES
test-affinity-dd4d5cff5-jbgx6   1/1     Running   0          15s   10.42.1.9   node1   *none*           *none*
test-affinity-dd4d5cff5-lpcv4   1/1     Running   0          15s   10.42.1.7   node1   *none*           *none*
test-affinity-dd4d5cff5-jsww7   1/1     Running   0          15s   10.42.1.8   node1   *none*           *none* 
```
   
## Taints and tolerations 

Node affinity is about attracting Pod to Nodes. Taints are to refuse pod to be scheduled unless that pod has a matching toleration. Taints are more like blacklist so when there are many nodes and need to blacklist one then it is really easy to achieve this with Taints [@KubeShedule-sp20-516-232]. 

* A taint applied to a node indicates that only specific pods can be scheduled on them.
* A toleration is applied to a pod allows them to tolerate a node's taint.

Taints and tolerations consist of a key, value, effect and operator

1. **Key**: The key is any string, up to 253 characters. The key must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.

2. **Value**: Value is any string, up to 63 characters. The value must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores. 

3. **Effect**: Effect can be 
    * NoSchedule: New pods that do not match the taint are not scheduled onto that node. Existing pods on the node remain.
    * PreferNoSchedule: New pods that do not match the taint might be scheduled onto that node, but the scheduler tries not to.Existing
                        pods on the node remain. 
    * NoExecute: New pods that do not match the taint cannot be scheduled onto that node.Existing pods on the node that do not have a                    matching toleration are removed.
 4. **Operator**:
    * Equal: The key/value/effect parameters must match. This is the default.
    * Exists: The key/effect parameters must match. You must leave a blank value parameter, which matches any.
    
 ### Taint Demo:
 
 Before applying taint on any node, try scheudling an App called busybox based on seeded image busybox.
 
```
 $ kubectl run before-taint --image busybox --replicas 4 -- sleep 99
```

We can observe that all the Nodes gets scheduled with pods:

```
$ kubectl get po -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP          NODE            NOMINATED NODE   READINESS GATES
before-taint-69c6778cfb-hznss   1/1     Running   0          15s   10.42.1.3   microk8s-vm-w1   *none*           *none*
before-taint-64fc5f64b7-qktdr   1/1     Running   0          15s   10.42.0.8   microk8s-vm-w3   *none*           *none*
before-taint-64fc5f64b7-5x6bt   1/1     Running   0          15s   10.42.0.5   microk8s-vm-w2   *none*           *none*
before-taint-69c6778cfb-267wm   1/1     Running   0          15s   10.42.0.4   microk8s-vm-w1   *none*           *none*
ubuntu@node1:~$  
```

Now taint one of the node for ex:microk8s-vm-w1 with effect:NoSchedule. This will stop scheduling of pods on the node:microk8s-vm-w1. 

```
$ kubectl taint node microk8s-vm-w1 node-type=production:NoSchedule
node/microk8s-vm-w1 tainted
```

Now try scheduling new pods. 

```
$ kubectl run test-taint --image busybox --replicas 4 -- sleep 99
kubectl run --generator=deployment/apps.v1 is DEPRECATED and will be removed in a future version. Use kubectl run --generator=run-pod/v1 or kubectl create instead.
deployment.apps/test-taint created
```

We can observe that microk8s-vm-w1 is not assigned with any Pods:

```
$ kubectl get po -o wide
NAME                         READY   STATUS    RESTARTS   AGE   IP          NODE            NOMINATED NODE   READINESS GATES
test-taint-dd4d5cff5-jbgx6   1/1     Running   0          19s   10.42.1.9   microk8s-vm-w2   *none*           *none*
test-taint-dd4d5cff5-lpcv4   1/1     Running   0          19s   10.42.1.7   microk8s-vm-w3   *none*           *none*
test-taint-dd4d5cff5-jsww7   1/1     Running   0          19s   10.42.1.8   microk8s-vm-w3   *none*           *none*
test-taint-64fc5f64b7-zxsh   1/1     Running   0          19s   10.42.1.8   microk8s-vm-w2   *none*           *none*
```

### Toleration Demo:

A toleration is how a pod declares that it can bypass a taint. It is basically a pass that will allow the pod onto any node with any taint. Define a deployment yaml file: podToleration.yaml with toleration as below. Make sure toeration matches with taint of node:microk8s-vm-w1. 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: with-toleration-app
  labels:
    app: nginx
spec:
 replicas: 6
 selector:
   matchLabels:
     app: nginx
 template:
   metadata:
      labels:
        app: nginx
   spec:
      containers:
      - name: nginx
        image: nginx:alpine
      tolerations:
      - key: "node-type"
        operator: "Equal"
        value: "production"
        effect: "NoSchedule"
```

Deploy the pod with toleration:
```
kubectl apply -f podToleration.yaml
deployment.apps/with-toleration-app created
```

Now query pods. We can observe that even though node:microk8s-vm-w1 is tainted, some of the pods are able to get scheudle on microk8s-vm-w1 because of toleration:

```
NAME                                  READY   STATUS    RESTARTS   AGE   IP          NODE             NOMINATED NODE   READINESS GATES
with-toleration-app-d9db86b77-flxw2   1/1     Running   0          19s   10.42.1.14   microk8s-vm-w2   *none*           *none*
with-toleration-app-d9db86b77-rhhg7   1/1     Running   0          19s   10.42.1.15   microk8s-vm-w1   *none*           *none*
with-toleration-app-d9db86b77-5bn76   1/1     Running   0          19s   10.42.1.16   microk8s-vm-w3   *none*           *none*
with-toleration-app-d9db86b77-wgmkf   1/1     Running   0          19s   10.42.0.29   microk8s-vm-w2   *none*           *none*
with-toleration-app-d9db86b77-xw7xq   1/1     Running   0          19s   10.42.0.28   microk8s-vm-w1   *none*           *none*
with-toleration-app-d9db86b77-bkdgw   1/1     Running   0          19s   10.42.0.30   microk8s-vm-w2   *none*           *none*
```

To remove taint we can use command:

```
kubectl taint nodes microk8s-vm-w1 node-type=NoSchedule-
```

## References

1. <https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/>  
2. <https://medium.com/@dominik.tornow/the-kubernetes-scheduler-cd429abac02f>
3. <https://thenewstack.io/implementing-advanced-scheduling-techniques-with-kubernetes/>
4. <https://docs.microsoft.com/en-us/azure/aks/operator-best-practices-advanced-scheduler>
