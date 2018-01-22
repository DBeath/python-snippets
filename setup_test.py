import os
import imp


def from_envvar(variable_name):
    rv = os.environ.get(variable_name)
    if not rv:
        raise RuntimeError('The environment variable %r is not set '
                           'and as such configuration could not be '
                           'loaded.  Set this variable and make it '
                           'point to a configuration file' %
                           variable_name)

    return


def from_pyfile(filename):
    d = imp.new_module('config')
    try:
        with open(filename) as config_file:
            exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
    except IOError as e:
        print(e)

    print(d.DOB)
    return d


obj = from_pyfile('test_config.py')
print(getattr(obj, 'NAME'))
