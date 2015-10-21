from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from social.backends.google import GoogleOAuth2
from xhtml2pdf import pisa             # import python module

# Create your views here.
def index(request):
	'''sourceHtml = "<html><body><h1>Functioneaza</h1></body></html>"
	outputFilename = "test.pdf"

	resultFile = open(outputFilename, "w+b")

	# convert HTML to PDF
	pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

	resultFile.close()                 # close output file

	# return True on success and False on errors
	if pisaStatus.err == False :
		print "Error"'''
	return render_to_response("index.html")

def base_to_img():
	import base64
	imgdata = base64.b64decode(imgstring)
	filename = 'some_image.jpg'
	with open(filename, 'wb') as f:
		f.write(imgdata)


# Define your data
#file = open("template.html")
#sourceHtml = file.read()

def save_profile(backend, user, response, *args, **kwargs):
    if isinstance(backend, GoogleOAuth2):
        if response.get('image') and response['image'].get('url'):
            url = response['image'].get('url')
            ext = url.split('.')[-1]
            user.avatar.save(
               '{0}.{1}'.format('avatar', ext),
               ContentFile(urllib2.urlopen(url).read()),
               save=False
            )
            user.save()

def profile(request):
	email = request.user.email
	print email
	user = UserProfile.objects.get(social_email=str(email))

	return render_to_response("profile.html",{"user":user})