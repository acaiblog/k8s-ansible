import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True, help='接受deploy/upgrade参数部署/升级k8s集群')
    args = parser.parse_args().__dict__
    logging.debug('args: %s' %args)
    return args

def cmd(action):
    logging.debug("action: %s" %action)
    os.system('ansible-playbook  -i inventory/hosts -e "action=%s" os-init.yaml' %action)
    os.system('ansible-playbook  -i inventory/hosts -e "action=%s" k8s.yaml' %action)

if __name__ == "__main__":
    cmd(args()['action'])
