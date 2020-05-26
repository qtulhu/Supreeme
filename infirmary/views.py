from django.shortcuts import render
from .models  import Doctor,Pacient,Diagnosis,Procedure

def index(request):


    pacients = Pacient.objects.all()

    all_pacient = []
    for index in pacients:
        pacient = {
            'ill': index,
            'first_name':index.first_name,
            'last_name':index.last_name,
            'age':index.age,
            'doctor':index.doctor,
            'diagnosis':index.diagnosis,
            'procedures':index.procedures,
            'pulse_link':index.pulse_link,
            'spo2_link':index.spo2_link,
            'pi_link':index.pi_link,
            'temperature_link':index.temperature_link,
            # 'link':index.get_absolute_url,
        }
        all_pacient.append(pacient)


    return render(
        request,
        'index.html',
        {'pacient_info':all_pacient},
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

def monitoring(request):
	return render(
	    request,
	    'monitoring.html',
	)
