from distutils.version import LooseVersion, StrictVersion
import operator as py_operator
from ansible.errors import AnsibleFilterError

def version_compare(value, version, operator='eq', strict=False):
    ''' Perform a version comparison on a value '''
    op_map = {
        '==': 'eq', '=':  'eq', 'eq': 'eq',
        '<':  'lt', 'lt': 'lt',
        '<=': 'le', 'le': 'le',
        '>':  'gt', 'gt': 'gt',
        '>=': 'ge', 'ge': 'ge',
        '!=': 'ne', '<>': 'ne', 'ne': 'ne'
    }

    if strict:
        Version = StrictVersion
    else:
        Version = LooseVersion

    if operator in op_map:
        operator = op_map[operator]
    else:
        raise AnsibleFilterError('Invalid operator type')

    try:
        method = getattr(py_operator, operator)
        return method(Version(str(value)), Version(str(version)))
    except Exception as e:
        raise AnsibleFilterError('Version comparison: %s' % e)


class FilterModule(object):
    def filters(self):
        return {'version_compare': version_compare}

