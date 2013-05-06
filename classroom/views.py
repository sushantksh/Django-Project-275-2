# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
# from classroom.models import posts
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json
import sys
#SQLite models 
from classroom.models import userTable
#from requests import session
import httpconnection
#SQLite-Django auth
from django.contrib.auth import logout


def signIn(request):
    return render(request, 'login.html')
    
# login to home page - This is called when user is in the DB and login is successful
def home(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

    payload = {'email':username,'pwd':password}
    data=json.dumps(payload)
    #static method call
    response = httpconnection.home_Connect(data)
    convertToJson = response.json()

    return render_to_response("home.html",convertToJson,context_instance=RequestContext(request))

# Sign Up function
def signUp(request):
    return render(request, 'signUp.html')

# signup_home page fucntion is called when there is new user entry
def signUpHome(request):
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	user = userTable(username=request.POST.get('username'), password=request.POST.get('password'),firstName=request.POST.get('firstname'),lastName=request.POST.get('lastname'))
	user.save()

    payload = { "email": username,"pwd": password,"fName": firstname,"lName": lastname} 
    data=json.dumps(payload)

    response = httpconnection.signUpHome_Connect(data)
    convertToJson = response.json()
    print convertToJson
    return render_to_response("home.html",convertToJson,context_instance=RequestContext(request))

# sign out function
def signOut(request):
    logout(request)
    return render(request, 'login.html')
    #resp = requests.get("http://localhost:8080/user/:email",data=json.dumps(payload))
    #print str(r)+" ---- > Call Back from Bottle Achieved "
    #convertToJson = response.json()
    #print convertToJson
    #return render_to_response("login.html",convertToJson,context_instance=RequestContext(request))    

######_________________________________ USER __________________________________ #######




















