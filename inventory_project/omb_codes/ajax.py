from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from django.utils import simplejson

from .models import Program_Code, Bureau_Code

@dajaxice_register
def present_agencies(request):
    dajax = Dajax()
    agencies = Program_Code.objects.distinct('agency')
    out = []
    for agency in agencies:
        out.append("<option value='%s'>%s</option>" % agency,agency)
    
    dajax.assign('#id_program_code', 'innerHTML', ''.join(out))
    return dajax.json()