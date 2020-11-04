from django.shortcuts import render, redirect
from .models import Drink, SeverityLevel
from .forms import GetInfo, RequestMeasurement, ImperialOrMetric, ResetTime
from boozelib import get_blood_alcohol_content, get_degradation

def get_measurement(request):
	# Get form
	form = ImperialOrMetric()
	context = {'form': form}

	# Form logic and taking data
	if request.method == "POST":
		form = ImperialOrMetric(request.POST)
		if form.is_valid():
			request.session['measurement'] = form.cleaned_data['measurement']
			return redirect('get-info')
			
	return render(request, 'main/metric-imperial.html', context)

def get_info(request):
	# Get form
	form = GetInfo()
	context = {}
	
	# Form logic and taking data
	if request.method == "POST":
		form = GetInfo(request.POST)
		if form.is_valid():
			request.session['weight'] = form.cleaned_data['weight']
			request.session['sex'] = form.cleaned_data['gender']
			request.session['age'] = form.cleaned_data['age']
			request.session['ate']= form.cleaned_data['ate']
			request.session['time'] = form.cleaned_data['time']
			request.session['height'] = form.cleaned_data['height']
			if request.session['measurement'] == "oz":
				request.session['height'] = request.session['height'] * 2.54
				request.session['weight'] = request.session['weight'] * 0.454
			request.session['drunk_level'] = -get_degradation(request.session['age'], request.session['weight'], request.session['height'], request.session['sex'], request.session['time']*60)
			if request.session['ate'] == True:
				request.session['drunk_level'] -= 0.1
			request.session['size'] = 0
			return redirect('index')
	else:
		form = GetInfo()

	context['form'] = form

	return render(request, 'main/get-info.html', context)
	

def index(request):
	
	# Get and add form to context
	form = RequestMeasurement()
	context = {'form':form}

	# Get all drinks and add to context
	drinks = Drink.objects.all()
	context['drinks'] = drinks

	# get status for Vue
	status = get_status(request.session['drunk_level'], request.session['size'])
	context['status'] = SeverityLevel.objects.get(severity=status)

	return render(request, 'main/index.html', context)


def add_drink(request, pk):
	# Get Model and Form
	data = Drink.objects.get(id=pk)
	form = RequestMeasurement()

	# Get size from form
	if request.method == "POST":
		form = RequestMeasurement(request.POST)
		if form.is_valid():
			request.session['size'] = form.cleaned_data['size']

	# Get session variables
	weight = request.session['weight']
	ate = request.session['ate']
	time = request.session['time']
	size = request.session['size']
	sex = request.session['sex']
	age = request.session['age']
	height = request.session['height']
	# Get percentage of alcahool 
	p = get_p(data.severity)

	# Measurement and sex check
	if request.session['measurement'] == "cl":
		size = size * 10
	elif request.session['measurement'] == "oz":
		size = size * 29.54
	sex_identification = True
	if sex == "M":
		sex_identification = False

	# Call the main function and store it for Vue
	request.session['drunk_level'] += get_blood_alcohol_content(age, weight, height, sex_identification, size, p)
	request.session['status'] = get_status(request.session['drunk_level'], request.session['size'])
	
	return redirect('index')

# Clear bac value
def clear_bac(request):
	request.session['size'] = 0
	request.session['drunk_level'] = -get_degradation(request.session['age'], request.session['weight'], request.session['height'], request.session['sex'], request.session['time']*50)
	if request.session['ate'] == True:
		request.session['drunk_level'] -= 0.1
	return redirect('index')

# Redo the forms
def redo_values(request):
	return redirect('get_measurement')

# Resets time for last drinks
def rest_time_last_drink(request):
	form = ResetTime()
	if request.method == "POST":
		form = ResetTime(request.POST)
		if form.is_valid():
			request.session['time'] = form.cleaned_data['time']
			request.session['check'] = form.cleaned_data['check']
			if request.session['check'] == True:
					request.session['drunk_level'] = -get_degradation(request.session['age'], request.session['weight'], request.session['height'], request.session['sex'], request.session['time']*60)
			return redirect('index')
	context = {'form': form}
	return render(request, 'main/reset-time.html', context)

def drink_info(request, pk):
	data = Drink.objects.get(id=pk)
	context = {'data':data}
	return render(request, 'main/drink-info.html', context)


# Function to get status from bac
def get_status(bac, size):
	if bac <= 0.4:
		if size > 0:
			return 1
		return 6
	elif bac <= 0.8:
		return 2
	elif bac <= 1.8:
		return 3
	elif bac <= 3.2:
		return 4
	else:
		return 5 

# Function to get percentage 
def get_p(severity):
	if severity == 1:
		p = 5.4
	elif severity == 2:
		p = 14
	else:
		p = 38
	return p
