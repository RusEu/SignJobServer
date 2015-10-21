from django.core.context_processors import request

def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
	url = None
	if backend.name == 'facebook':
	    url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
	if backend.name == 'google-oauth2':
	    print response['id']
	    print response['image'].get('url')
	    print response['emails'][0]["value"]
	    print response['displayName']
	    #first_name 
	    print response['name']['givenName']
	    #last_name
	    print response['name']['familyName']
	    print response['gender']
	    print response['language']