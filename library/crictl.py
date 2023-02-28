#!/usr/bin/python
from ansible.module_utils.basic import *
import subprocess
import logging

def start_container(name):
    cmd = ['nerdctl', 'run', '--name', name, 'busybox']
    result = subprocess.check_output(cmd)
    return result

def stop_container(name):
    cmd = ['nerdctl', 'stop', name]
    result = subprocess.check_output(cmd)
    return result

def image_pull(image_name,tag):
    cmd = ['nerdctl', 'pull', '%s:%s' %(image_name,tag)]
    result = subprocess.check_output(cmd)
    return result

def image_tag(name,repository):
    cmd = ['nerdctl', 'tag', name, repository]
    result = subprocess.check_output(cmd)
    return result

def image_rmi(name,repository):
    cmd = ['nerdctl', 'rmi', name,repository]
    result = subprocess.check_output(cmd)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=False),
            state=dict(choices=['started', 'stopped', 'pull']),
            image=dict(required=False),
            tag=dict(required=False),
            repository=dict(required=False),
            source=dict(choices=['local'], default='local')
        )
    )

    name = module.params['name']
    state = module.params['state']
    image_name = module.params['image']
    tag = module.params['tag']
    source = module.params['source']
    repository = module.params['repository']

    if state == 'started':
        output = start_container(name)
        module.exit_json(changed=True, msg=output)
    elif state == 'pull':
        output = image_pull(image_name,tag)
        module.exit_json(changed=True, msg=output)
    elif source == 'local':
        output = image_tag(name,repository)
        module.exit_json(changed=True, msg=output)
    else:
        output = stop_container(name)
        module.exit_json(changed=True, msg=output)

if __name__ == '__main__':
    main()

