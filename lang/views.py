from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    trans = _('hello')
    return render(request, 'templates/base.html', {'trans': trans})