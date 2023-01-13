# 支持以下功能
- 支持部署docker
- 支持部署k8s v1.14.0版本
- 支持calico网络插件，calico release参考：[link](https://projectcalico.docs.tigera.io/releases#)，calico支持的k8s版本参考下表：

| calico版本        | k8s版本          | 参考链接                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------|
| v3.7            | 1.12/1.13/1.14 | [calico v3.7](https://projectcalico.docs.tigera.io/archive/v3.7/getting-started/kubernetes/requirements)   |
| v3.8/v3.9/v3.10 | 1.13/1.14/1.15 | [calico v3.9](https://projectcalico.docs.tigera.io/archive/v3.9/getting-started/kubernetes/requirements)   |
| v3.11           | 1.14/1.15/1.16 | [calico v3.11](https://projectcalico.docs.tigera.io/archive/v3.11/getting-started/kubernetes/requirements) |
| v3.12           | 1.14/1.15/1.16/1.17 | [calico v3.12](https://projectcalico.docs.tigera.io/archive/v3.12/getting-started/kubernetes/requirements) |
| v3.13           | 1.15/1.16/1.17 | [calico v3.13](https://projectcalico.docs.tigera.io/archive/v3.13/getting-started/kubernetes/requirements) |
| v3.14/v3.15     | 1.16/1.17/1.18 | [calico v3.14](https://projectcalico.docs.tigera.io/archive/v3.14/getting-started/kubernetes/requirements) |
| v3.16           | 1.16/1.17/1.18/1.19 | [calico v3.16](https://projectcalico.docs.tigera.io/archive/v3.16/getting-started/kubernetes/requirements) |
| v3.17           | 1.17/1.18/1.19 | [calico v3.17](https://projectcalico.docs.tigera.io/archive/v3.17/getting-started/kubernetes/requirements) |
| v3.18           | 1.18/1.19/1.20 | [calico v3.18](https://projectcalico.docs.tigera.io/archive/v3.18/getting-started/kubernetes/requirements) |
| v3.19/v3.20     | 1.19/1.20/1.21 | [calico v3.19](https://projectcalico.docs.tigera.io/archive/v3.19/getting-started/kubernetes/requirements) |
| v3.21           | 1.20/1.21/1.22 | [calico v3.21](https://projectcalico.docs.tigera.io/archive/v3.21/getting-started/kubernetes/requirements) |
| v3.22/v3.23     | 1.21/1.22/1.23 | [calico v3.22](https://projectcalico.docs.tigera.io/archive/v3.22/getting-started/kubernetes/requirements) |
| v3.24           | 1.22/1.23/1.24/1.25 | [calico v3.24](https://projectcalico.docs.tigera.io/archive/v3.24/getting-started/kubernetes/requirements) |

# 配置ansible环境

拉取ansible脚本
```
yum install -y git
git clone https://gitee.com/acaiblog/ansible-k8s.git
```
安装pypi包
```
yum install -y python3 sshpass
pip3 install virtualenv
virtualenv ansible-env
source /root/ansible-env/bin/activate
pip3 install -r ansible-k8s/requestments.txt
```
进入ansible-k8s目录，按照环境修改group_vars和inventory配置，执行节点初始化
```
cd /root/ansible-k8s/
ansible-playbook  -i inventory/hosts os-init.yaml
```
部署k8s集群
```
cd /root/ansible-k8s/
ansible-playbook  -i inventory/hosts k8s.yaml
```