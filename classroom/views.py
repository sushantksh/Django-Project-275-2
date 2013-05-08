# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
# from classroom.models import posts
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json
import sys

from django.contrib.auth import logout

#from requests import session
import httpconnection
#SQLite-Django auth
from django.contrib.auth import logout
#SQLite models 
#from classroom.models import userTable
#from requests import session
import httpconnection
from django.contrib.auth import logout
from django.contrib.auth.models import User


def signIn(request):
    return render(request, 'login.html')
    
# login to home page - This is called when user is in the DB and login is successful
def home(request):
  state = "Please log in below..."
  username = password = ''
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']
    print username
    print password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            state = "You're successfully logged in!"
            print state
        else:
            state = "Your account is not active, please contact the site admin."
            print state
    else:
        state = "Your username and/or password were incorrect."
        print state

  return render_to_response('home.html', {'state': state, 'username': username})
    



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
        user = User.objects.create_user(username, '', password)
        user.last_name = lastname
        user.first_name= firstname
        user.save()

    payload = { "email": username,"pwd": password,"fName": firstname,"lName": lastname} 
    data=json.dumps(payload)

    response = httpconnection.signUpHome_Connect(data)
    print "response status code = ", response.status_code
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

#def getUser(request):
    # Get email id of user from html
 #   resp = requests.get(url+user+"email")




















