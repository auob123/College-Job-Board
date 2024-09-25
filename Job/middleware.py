# Job/middleware.py

from django.utils import translation
from django.shortcuts import redirect

class LanguageRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the path is the root `/`
        if request.path == '/':
            # Get the user's language preference or fallback to default
            language = translation.get_language_from_request(request, check_path=False)
            return redirect(f'/{language}/')  # Redirect to language-prefixed URL

        response = self.get_response(request)
        return response
