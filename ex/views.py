from django.http import HttpResponse

def getFile(request):
	content = 'a new file \n'
	response = HttpResponse(content, content_type = 'text/plain')
	response['content-Disposition'] = 'attachment; filename = "newfile.txt"'
	return response
