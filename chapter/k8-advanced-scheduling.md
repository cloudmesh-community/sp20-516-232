# Advanced Scheduling in Kubernetes sp20-516-232, Singam, Ashok

## Node affinity to attract pods  

Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. The rules are defined using custom labels on nodes and label selectors specified in pods. Node affinity allows a pod to specify an affinity (or anti-affinity) towards a group of nodes it can be placed on. The node does not have control over the placement. 

For example, you could configure a pod to only run on a node with a specific CPU or in a specific availability zone. There are two types of node affinity rules: 

* Required 
* preferred

Required rules must be met before a pod can be scheduled on a node. Preferred rules specify that, if the rule is met, the scheduler tries to enforce the rules, but does not guarantee enforcement.

### Configuring Node Affinity
One can configure node affinity through the pod specification file. We can specify a required rule, a preferred rule, or both. If you specify both, the node must first meet the required rule, then attempts to meet the preferred rule.

## Using taints and tolerations to repel pods from certain nodes


