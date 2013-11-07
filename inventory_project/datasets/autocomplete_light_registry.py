import autocomplete_light
from models import Tag

class TagAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name']
    autocomplete_js_attributes={'placeholder': 'Other model name ?',}
    model = Tag
autocomplete_light.register(TagAutocomplete)