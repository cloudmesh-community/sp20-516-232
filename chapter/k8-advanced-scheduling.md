# Advanced Scheduling Kubernetes sp20-516-232, Singam, Ashok

:o2: test: How do you include images in markdown for the books?

:o2: test: how do you do verbatim/code

:o2: test: what cames before and after a code block?

answer:

```bash
$ ls # this is a terminal command see the $ at the start
```

```
this is code
```

:o2: test: why can you not write `< none >` without spaces `

Advanced Scheduling fetatures makes Kubernetes a very flexible,policy-rich, topology-aware, workload-specific scheduler. These features provide a wide range of options to specify conditions for assigning pods to particular worker nodes that satisfy a condition. With advanced Scheduling features one can influence where pods can be scheduled among availalbe Nodes. In Kubernetes 1.6 four advanced scheduling features are added. Scope of this chapter is limited to first two features. 

1. Node affinity
2. Taints and tolerations, 
3. Pod affinity/anti-affinity 
4. Custom schedulers. 

## Node affinity to attract pods  

Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. The rules are defined using custom labels on nodes and label selectors specified in pods. Node affinity allows a pod to specify an affinity (or anti-affinity) towards a group of nodes it can be placed on. The node does not have control over the placement. 

For example, you could configure a pod to only run on a node with a specific CPU or in a specific availability zone. There are two types of node affinity rules: 

* Required 
* preferred

Required rules must be met before a pod can be scheduled on a node. Preferred rules specify that, if the rule is met, the scheduler tries to enforce the rules, but does not guarantee enforcement.

@fig:sp20-516-232-NodeAffinity illustrates scheduling based node affinity 

:o2: you did the image wrong, look it up in our notation.md file most all books have it

:o2: images/nodeAffinity.png

### Node affinity example

Print list of the nodes

```
NAME    STATUS    ROLES     AGE       VERSION
node1   Ready     <none>    5m        v1.9.4
node2   Ready     <none>    5m        v1.9.4
```

Now label node1 as Size:M1

```
kubectl label nodes node1 node1=Size:M1
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

```
kubectl run  test-affinity --image busybox --replicas 4 -- sleep 99
```

We can observe that all the pods are scheduled on node1. No pod is scheduled on node2!

```
ubuntu@node1:~$ kubectl get po -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP          NODE    NOMINATED NODE   READINESS GATES
test-affinity-dd4d5cff5-jbgx6   1/1     Running   0          15s   10.42.1.9   node1   < none >           < none >
test-affinity-dd4d5cff5-lpcv4   1/1     Running   0          15s   10.42.1.7   node1   < none >           < none >
test-affinity-dd4d5cff5-jsww7   1/1     Running   0          15s   10.42.1.8   node1   < none >           < none >
```
   
## Using taints and tolerations to repel pods from certain nodes

Node affinity is about attracting Pod to Nodes. Taints are to refuse pod to be scheduled unless that pod has a matching toleration. Taints are more like blacklist so when there are many nodes and need to blacklist one then it is really easy to achieve this with Taints. 

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
    
 @fig:sp20-516-232-Taint illustrates scheduling based node taints 

:o2: images/taint.png

    
 ### Taint Example:
 
 Setup a cluster with two nodes say node1 and node2. Before applying taint, try scheudling pods.
 
```
 kubectl run before-taint --image busybox --replicas 2 -- sleep 99
```

We can observe that both Nodes gets scheduled with pods:

```
ubuntu@node1:~$ kubectl get po -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP          NODE    NOMINATED NODE   READINESS GATES
before-taint-69c6778cfb-hznss   1/1     Running   0          15s   10.42.1.3   node2   < none >           < none >
before-taint-69c6778cfb-267wm   1/1     Running   0          15s   10.42.0.8   node1   < none >           < none >
ubuntu@node1:~$  
```

Taint node1 with effect:NoSchedule. This will stop new pods that will not match taint. 

```
ubuntu@node1:~$ kubectl taint node node1 node-type=production:NoSchedule
node/node1 tainted
```

Now try scheduling new pods. 

```
ubuntu@node1:~$ kubectl run test-taint --image busybox --replicas 3 -- sleep 99
kubectl run --generator=deployment/apps.v1 is DEPRECATED and will be removed in a future version. Use kubectl run --generator=run-pod/v1 or kubectl create instead.
deployment.apps/test-taint created
```

We can observe that only node2 is scheduled with new Pods:

```
ubuntu@node1:~$ kubectl get po -o wide
NAME                         READY   STATUS    RESTARTS   AGE   IP          NODE    NOMINATED NODE   READINESS GATES
test-taint-dd4d5cff5-jbgx6   1/1     Running   0          19s   10.42.1.9   node2   < none >         < none >
test-taint-dd4d5cff5-lpcv4   1/1     Running   0          19s   10.42.1.7   node2   < none >         < none >
test-taint-dd4d5cff5-jsww7   1/1     Running   0          19s   10.42.1.8   node2   < none >         < none >
```

## References

1. <https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/>  
2. <https://medium.com/@dominik.tornow/the-kubernetes-scheduler-cd429abac02f>
3. <https://thenewstack.io/implementing-advanced-scheduling-techniques-with-kubernetes/>
4. <https://docs.microsoft.com/en-us/azure/aks/operator-best-practices-advanced-scheduler>
