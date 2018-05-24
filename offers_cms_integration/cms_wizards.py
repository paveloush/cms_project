from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from offers_cms_integration.forms import EstateWizardForm


class EstateWizard(Wizard):
    pass

estate_wizard = EstateWizard(
    title="Estate",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=EstateWizardForm,
    description="Create a new Offer",
)

wizard_pool.register(estate_wizard)