from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from offers_cms_integration.models import EstatePluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin
class OfferPluginPublisher(CMSPluginBase):
    model = EstatePluginModel
    module = _('Offers')
    name = _('Estate Plugin')
    render_template = 'offers_cms_integration/estate_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return (context)
