import pkg_resources
import yaml

DEFAULTS = yaml.safe_load(pkg_resources.resource_string(__name__, "config.yml"))
