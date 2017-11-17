from django.shortcuts import render

# Create your views here.

#Import SignupForm from the forms folder
from .forms import SignupForm

#Creating the signupform view - logically decides what to show
def signupform (request) :
    
    #if the request has a POST method
    if request.method == 'POST' :
        #create the form and pass in the POST
        form = SignupForm(request.POST)
        
        #Check if the fields in form are accurate
        if form.is_valid():
            #display the result page and pass in the values
            return render(request, 'result.html', {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email']
            })
        
        #if the fields are empty or not valid, stay on the same page and display errors    
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form })
    
    #if it's not a POST method, i.e. first time loading the site
    else :
        #create an empty SignupForm
        form = SignupForm()
        
        #And, render the signup page and pass in the form variable containing the SignupForm template
        return render(request, 'signup.html', {'form':form});
    