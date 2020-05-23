from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
    )


def add(request):
	return render(
	    request,
	    'add-pacient.html',
	)


def pacient(request):
	return render(
	    request,
	    'pacient.html',
	)

def archive(request):
	return render(
	    request,
	    'archive.html',
	)

def help(request):
	return render(
	    request,
	    'help.html',
	)
