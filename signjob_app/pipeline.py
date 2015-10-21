from django.core.context_processors import request
from django.contrib.auth.models import User
from user_profile.models import UserProfile

def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
	url = None
	if backend.name == 'facebook':
	    url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
	if backend.name == 'google-oauth2':
		try:
	   		UserProfile.objects.get(social_email=str(response['emails'][0]["value"]))
	   	except UserProfile.DoesNotExist:
			UserProfile.objects.create(social_id = response['id'],
	                                 social_alias = str(response['displayName']),
	                                 social_first_name = str(response['name']['givenName']),
	                                 social_last_name = str(response['name']['familyName']),
	                                 social_email = str(response['emails'][0]["value"]),
	                                 social_gender = str(response['gender']),
	                                 social_language = str(response['language']),
	                                 social_avatar = str(response['image'].get('url')),
	                                 )