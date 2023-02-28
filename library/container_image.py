#!/usr/bin/python

DOCUMENTATION = '''
---
module: container_image
author: Your Name <yourname@example.com>
version_added: "1.0"  # 最初添加的Ansible版本
short_description: 下载、删除、打标签和上传Containerd镜像。
description:
    - 该模块可用于下载、删除、打标签和上传Containerd镜像。
options:
    name:
        description:
            - 要下载、删除、打标签或上传的Containerd镜像的名称。
        required: true
    state:
        description:
            - Containerd镜像的状态。如果为present，则拉取镜像到本地；如果为absent，则删除本地镜像；如果为push，则上传镜像到远程仓库；如果为tag
        choices: ['present', 'absent', '', 'push']
        required: true
    tag:
        description:
            - 指定镜像标签
        required: false
    image_tag:
        description:
            - 要应用于Containerd镜像的标记。如果不需要打标签则不需要该选项；如果需要打标签则tag为<repository>/<image_name>:<tag>
    repository:
        description:
            - Containerd镜像的仓库名称。
        required: true

notes:
    - 此模块需要在目标主机上安装Containerd和nerctl。
    - 如果选择上传Containerd镜像，必须提供Containerd API密钥。
'''

from ansible.module_utils.basic import *
import subprocess
import logging

def image_download(repository,name,tag):
    cmd = ['nerctl', 'pull', '{}/{}:{}'.format(repository, name, tag)]
    res = subprocess.check_output(cmd)
    return res

def image_upload(repository,name,tag):
    cmd = ['nerctl', 'push', '{}/{}:{}'.format(repository, name, tag)]
    res = subprocess.check_output(cmd)
    return res

def image_destroy(repository,name,tag):
    cmd = ['nerctl', 'rmi', '{}/{}:{}'.format(repository, name, tag)]
    res = subprocess.check_output(cmd)
    return res

def image_tag(repository,name,tag,image_tag):
    cmd = ['nerctl', 'tag', '{}/{}:{}'.format(repository, name, tag), '{}'.format(image_tag)]
    res = subprocess.check_output(cmd)
    return res


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
            state=dict(choices=['present', 'absent', 'tag', 'push']),
            tag=dict(type='str'),
            image_tag=dict(type='str'),
            repository=dict(type='str'),
        )
    )

    name = module.params['name']
    state = module.params['state']
    tag = module.params['tag']
    image_tag = module.params['image_tag']
    repository = module.params['repository']

    if state == 'present':
        output = image_download(repository,name,tag)
        module.exit_json(changed=True,msg=output)
    elif state == 'absent':
        output = image_destroy(repository,name,tag)
        module.exit_json(changed=True,msg=output)
    elif state == 'push':
        output = image_upload(repository,name,tag)
        module.exit_json(changed=True,msg=output)
    elif tag:
        output = image_tag(repository,name,tag,image_tag)
        module.exit_json(changed=True, msg=output)


if __name__ == '__main__':
    main()
