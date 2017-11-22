from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, HttpResponse, render_to_response, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from .models import Plants, User, Temp, Soil, Actuator, Rain, Water


'''This function is to get data from Raspberrypi and to store in Django database.'''


def getdata(request):
    temp = request.GET['t']
    level = request.GET['cm']
    moisture = request.GET['m']
    ui = request.GET['uid']
    act = request.GET['act']
    i = request.GET['id']
    user = User.objects.filter(name=ui)[0]
    plant = Plants.objects.filter(plant_name=i, uid=user)[0]
    obj = Temp(pid = plant, temp = temp, dt = datetime.now())
    obj.save()
    obj = Water(uid = user, level = level, dt = datetime.now())
    obj.save()
    obj = Soil(pid = plant, m_level = moisture, dt = datetime.now())
    obj.save()
    obj = Actuator(pid = plant, status = act, dt = datetime.now())
    obj.save()


    return HttpResponse('this is a get request')

'''This function is to register user in the web-app'''


def signup(request):
    return render(request, 'Plant/signup-page.html', {})

'''This function is to Log user in the web-app'''


def login(request):
    return render(request, 'Plant/login-page.html', {})

'''This function is takes values from sign-in page and makes a user object in django database'''


def makeUser(request):
    try:
        alluser = User.objects.all()
        uobj = User()
        uobj.name = '_'.join(request.POST['name'].split())
        uobj.email = request.POST['email']
        for user in alluser:
            if user.email == uobj.email:
                return render(request, 'Plant/signup-page.html', {'error': 'error'})
        uobj.password = request.POST['password']
        uobj.save()
        return redirect('Plant:home', uobj.name)
    except MultiValueDictKeyError:
        return render(request, 'Plant/error-page.html', {})

'''This function is to log user in after checking whether the email-id and password is valid'''


def userprofile(request):
    try:
        st = request.POST['email']
        pt = request.POST['password']
        allusers = User.objects.all()
        for users in allusers:
            if users.email == st and users.password == pt:
                return redirect('Plant:home', users.name)
        return render(request, 'Plant/login-page.html', {'error': 'Invalid email-id or password', })
    except MultiValueDictKeyError:
        return render(request, 'Plant/error-page.html', {})

'''This function is to reload the profile page of user.'''


def home(request, name='none'):
    a = []
    if name is 'none':
        return userprofile(request)
    else:
        uobj = User.objects.get(name=name)
        plant_list = uobj.plants_set.order_by('dt')
        water_list = uobj.water_set.order_by('dt')[:10]
        rain_list = uobj.rain_set.order_by('dt')[:10]
        for plant in plant_list:
            a.append(plant.actuator_set.order_by('dt')[:1])
        return render(request, 'Plant/profile-page.html',
                      {'name': name, 'plant_list': plant_list, 'water_list': water_list, 'rain_list': rain_list, 'act_list': a})

'''This function is to log user out to the landing page.'''


def logout(request):
    return HttpResponseRedirect(reverse('Plant:login'))

'''This function is to go to respective plant page after user has selected the plant in plant list.'''


def userPlants(request, name, plant_name):
    user = User.objects.get(name=name)
    plant = Plants.objects.get(plant_name=plant_name, uid=user.id)
    temp_list = plant.temp_set.order_by('dt')[:10]
    soil_list = plant.soil_set.order_by('dt')[:10]
    return render(request, 'Plant/graph_sensor_values.html', {'temp_list': temp_list, 'soil_list': soil_list})

'''This function is to add a plant give by the user in profile page.'''


def addplant(request, name):
    uobj = User.objects.get(name=name)
    plant_name = request.POST['plant_name']
    lat = request.POST['lat']
    long = request.POST['long']
    plant = uobj.plants_set.create(plant_name=plant_name, lat=lat, lon=long)
    plant.save()
    return redirect('Plant:home', uobj.name)


'''This function is to edit the parameters of user such as username, email-id and password.'''


def editUser(request, name):
    user = User.objects.get(name=name)
    n = request.POST['name']
    if str(n) is not '':
        user.name = n
    e = request.POST['email']
    if str(e) is not '':
        user.email = e
    p = request.POST['passwd']
    if str(p) is not '':
        user.password = p
    user.save()
    return redirect('Plant:home', user.name)
