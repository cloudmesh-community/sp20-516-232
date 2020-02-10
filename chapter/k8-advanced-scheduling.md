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

Node affinity is about attracting Pod to Nodes. Taints are to refuse pod to be scheduled unless that pod has a matching toleration. Taints are more like blacklist so when there are many nodes and need to blacklist one then it is really easy to achieve this with Taints. 

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


