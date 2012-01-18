from django import template
from django.utils import simplejson


from javascript_configuration.configuration_builder import DEFAULT_CONFIGURATION_BUILDER


register = template.Library()

@register.tag(name='javascript_configuration')
def do_javascript_configuration(parser, token):
    """
        Returns a node with generated configuration.
    """
    return JavascriptConfigurationNode()


class JavascriptConfigurationNode(template.Node):
    """
        Represents a node that renders JavaScript configuration.
    """

    def __init__(self):
        pass

    def render(self, context):
        """
            Renders JS configuration.
        """
        return 'var configuration = ' + simplejson.dumps(
                DEFAULT_CONFIGURATION_BUILDER.get_configuration()) + ';'

