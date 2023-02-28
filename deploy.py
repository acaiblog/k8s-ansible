# coding=utf-8
import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True, help='接受osinit/deploy/upgrade/destroy参数初始化/部署/升级/清理k8s集群')
    args = parser.parse_args().__dict__
    return args

def deploy():
    os.system('ansible-playbook  -i inventory/hosts -e "k8s_action=%s" os-init.yaml' %action)
    os.system('ansible-playbook  -i inventory/hosts -e "k8s_action=%s" k8s.yaml' %action)

def upgrade():
    os.system('ansible-playbook  -i inventory/hosts -e "k8s_action=%s" k8s.yaml' %action)

def destroy():
    os.system('ansible-playbook -i inventory/hosts k8s-clear.yaml')

def osinit():
    os.system('ansible-playbook  -i inventory/hosts -e "k8s_action=%s" os-init.yaml' %action)

if __name__ == "__main__":
    action = args()['action']
    locals()[action]()
