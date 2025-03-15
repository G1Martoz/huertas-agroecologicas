from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/login/', '/register/'] and request.method == 'POST':
            ip = request.META.get('REMOTE_ADDR')
            key = f'rate_limit_{ip}'
            
            # Get the current attempts count and timestamp
            attempts = cache.get(key, {'count': 0, 'timestamp': timezone.now()})
            
            # Reset count if more than 1 hour has passed
            if timezone.now() - attempts['timestamp'] > timedelta(hours=1):
                attempts = {'count': 0, 'timestamp': timezone.now()}
            
            # Increment attempt count
            attempts['count'] += 1
            cache.set(key, attempts, 3600)  # Store for 1 hour
            
            # Block if too many attempts
            if attempts['count'] > 5:
                return HttpResponseForbidden('Too many attempts. Please try again later.')
        
        return self.get_response(request)