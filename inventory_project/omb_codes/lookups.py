from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Program_Code, Bureau_Code

class BureauCodeLookup(ModelLookup):
    model = Bureau_Code
    search_fields = (
        'department__icontains',
        'agency__icontains',
    )

    def get_item_value(self, item):
        # Display for currently selected item
        return u"%s -- %s" % (item.agency, item.department)

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s -- %s" % (item.agency, item.department)

class ProgramCodeLookup(ModelLookup):
    model = Program_Code
    search_fields = (
        'agency__icontains',
        'program_name__icontains',
    )

    def get_item_value(self, item):
        # Display for currently selected item
        return u"%s -- %s" % (item.agency, item.program_name)

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s -- %s" % (item.agency, item.program_name)

registry.register(ProgramCodeLookup)
registry.register(BureauCodeLookup)