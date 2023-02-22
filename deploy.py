import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True, help='接受deploy/upgrade/destroy参数部署/升级/清理k8s集群')
    args = parser.parse_args().__dict__
    logging.debug('args: %s' %args)
    return args

def cmd(action):
    logging.debug("action: %s" %action)
    if action != 'destroy':
      os.system('ansible-playbook  -i inventory/hosts -e "action=%s" os-init.yaml' %action)
      os.system('ansible-playbook  -i inventory/hosts -e "action=%s" k8s.yaml -v' %action)
    elif action == 'destroy':
      os.system('ansible-playbook -i inventory/hosts k8s-clear.yaml')

def destroy():
    os.system('ansible-playbook -i inventory/hosts k8s-clear.yaml')

if __name__ == "__main__":
    action = args()['action']
    if action == 'deploy' or 'upgrade':
      cmd(action)
    elif action == 'destroy':
      cmd(action)
