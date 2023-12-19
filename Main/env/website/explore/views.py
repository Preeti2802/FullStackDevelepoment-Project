from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from .forms import UserForm
from .models import User
from .old_llm_fsd import ask_function_calling
# myapp/views.py
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm  # Make sure to import your UserForm
# Create your views here.


def LandingPage(request):
    print("Page is rendered")
    if request.method == 'POST':
        username_login = request.POST.get('username_login')
        password_login = request.POST.get('password_login')
        print(username_login,password_login)

        try:
            user = User.objects.get(email=username_login, password=password_login)
            # If the user is found and password matches
            print(user)
            print("success")
            return render(request,'AfterRegistration.html')

        except User.DoesNotExist:
            # If no user is found
            return print({"success": False, "message": "Invalid credentials"}, status=401)
    return render(request,'LandingPage.html')

def AfterRegistration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # If you want to set a cookie and then redirect:
            #response = redirect('AfterRegistration.html')  # Redirect to a success page or another relevant page
            #response.set_cookie('username', request.POST['full_name'], max_age=1209600)  # 2 weeks
            #return response

            #Alternatively, if you want to render the same page with a success message:
            response = render(request, 'AfterRegistration.html', {'form': form, 'message': 'Registration successful'})
            response.set_cookie('username', request.POST['full_name'], max_age=1209600)  # 2 weeks
            return response
        else:
            # Form is not valid, render the page with form errors
            return render(request, 'AfterRegistration.html', {'form': form})
    else:
        # GET request, display empty form
        form = UserForm()
        return render(request, 'AfterRegistration.html', {'form': form})



def explore(request):
    return render(request,'explore.html')
def quiz(request):
    return render(request,'quiz.html')
def explore(request):
    return render(request,'explore.html')
def quiz(request):
    return render(request,'quiz.html')
def c1(request):
    return render(request,'c1.html')
def c2(request):
    return render(request,'c2.html')
def c3(request):
    return render(request,'c3.html')
def c4(request):
    return render(request,'c4.html')
def c5(request):
    return render(request,'c5.html')
def c6(request):
    return render(request,'c6.html')
def c7(request):
    return render(request,'c7.html')
def c8(request):
    return render(request,'c8.html')
def c9(request):
    return render(request,'c9.html')
def c10(request):
    return render(request,'c10.html')
def c11(request):
    return render(request,'c11.html')
def c12(request):
    return render(request,'c12.html')
def c13(request):
    return render(request,'c13.html')
def c14(request):
    return render(request,'c14.html')
def c15(request):
    return render(request,'c15.html')
def c16(request):
    return render(request,'c16.html')
def c17(request):
    return render(request,'c17.html')
def c18(request):
    return render(request,'c18.html')

from django.shortcuts import render



def result(request):
    if request.method == 'POST':
        responses = [
            request.POST.get('q1'),
            request.POST.get('q2'),
            request.POST.get('q3'),
            request.POST.get('q4'),
            request.POST.get('q5'),
            request.POST.get('q6'),
            request.POST.get('q7'),
            request.POST.get('q8'),
            request.POST.get('q9'),
            request.POST.get('q10'),
            request.POST.get('q11'),
            request.POST.get('q12'),
            request.POST.get('q13'),
            request.POST.get('q14'),
            request.POST.get('q15'),
            request.POST.get('q16'),
            request.POST.get('q17')
        ]

        questions = [
            "Do you like software coding?",
            "Do you like probability and statistics?",
            "Do you like hardware programming?",
            "Do you like circuits and its design?",
            "Do you like communications technologies?",
            "Do you like material sciences?",
            "Do you like manufacturing?",
            "Do you like urban planning and development?",
            "Do you enjoy studying algorithms and data structures?",
            "Do you prefer working on software development over hardware?",
            "Would you like to explore the field of artificial intelligence and machine learning?",
            "Are you interested in signal processing and VLSI systems?",
            "Do you like experimenting with IoT devices?",
            "Are you interested in geotechnical engineering and soil mechanics?",
            "Do you enjoy working on mechanical design and CAD?",
            "Do you want to explore the realm of power system and transmission?",
            "Would you prefer to work on projects related to web development and cyber security?"
        ]

        # Concatenate the questions with their corresponding responses
        response_string = ", ".join(f"{question} {response}" for question, response in zip(questions, responses))

        # Save the string in your model or process it
        output = ask_function_calling(response_string)
        print(output)

        return render(request, 'result.html', {'response_string': response_string, 'output': output})

    return render(request, 'error.html', {'message': 'Invalid request method'})

'''
def result(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')
        q11 = request.POST.get('q11')
        q12 = request.POST.get('q12')
        q13 = request.POST.get('q13')
        q14 = request.POST.get('q14')
        q15 = request.POST.get('q15')
        q16 = request.POST.get('q16')
        q17 = request.POST.get('q17')

        # Concatenate the values into a string
        response_string = f" {q1}, {q2}, {q3}, {q4}, {q5},  {q6},  {q7}, {q8},{q9},{q10},{q11},{q12},{q13},{q14},{q15},{q16},{q17}"

        responses = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17]
        questions = [
            "Do u like software coding?",
            "Do u like probability and statistics?",
            "Do u like hardware programming?",
            "Do u like circuits and its design?",
            "Do u like  communications technologies?",
            "Do u like material sciences?",
            "Do u like manufacturing?",
            "Do you like urban planning and development? ",
            "Do you enjoy studying algorithms and data structures",
            "Do you prefer working on software development over hardware?",
            "Would you like to explore the field of artificial intelligence and machine learning?",
            "Are you interested in signal processing and VLSI systems?",
            "Do you like experimenting with IoT devices?",
            "Are you interested in geotechnical engineering and soil mechanics?",
            "Do you enjoy working on mechanical design and CAD?",
            "Do u want to explore the realm of power system and transmission?",
            "Would you prefer to work on projects related to web development and cyber security?"
        ]

        loaded_model = joblib.load("FSD.pkl")
        new_data = pd.DataFrame([responses], columns=questions)
        prediction = loaded_model.predict(new_data)

        # Map predictions to categories using the actual prediction value
        category_mapping = {
            0: "in AI",
            1: "in CSE",
            2: "in Civil",
            3: "in ECE",
            4: "in EEE",
            5: "in ME",
        }

        # Get the category based on the prediction
        category = category_mapping.get(prediction[0], "Unknown")

        # Print the mapped category
        print("Mapped Category:", category)

        return render(request, 'result.html', {'response_string': response_string, 'category': category})
    '''