import autocomplete_light

from .models import Tag

class TagAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name']
autocomplete_light.register(Tag, TagAutocomplete)