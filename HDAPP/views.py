from django.shortcuts import render
from joblib import load

model=load('./savedModels/model.joblib')

def predictor(request):
    return render(request,'main.html',{'data':model})

def formInfo(request):
    if request.method == 'POST':
        try:
            age = float(request.POST.get('age'))
            sex = float(request.POST.get('sex'))
            cp = float(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = float(request.POST.get('fbs'))
            restecg = float(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            ca = float(request.POST.get('ca'))
            thal = float(request.POST.get('thal'))
            
            # Predict using your model
            y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, ca, thal]])
            
            if y_pred == 1:
                y_pred = 'YES'
            else:
                y_pred = 'NO'
        except ValueError:
            # Handle input conversion errors here
            y_pred = 'Invalid input'

        return render(request, 'result.html', {'result': y_pred})
    else:
        # Handle GET requests here
        return render(request, 'result.html')

# def result(request):
#     if request.method == 'POST':cls
#         age = float(request.POST.get('age'))
#         sex = float(request.POST.get('sex'))
#         cp = float(request.POST.get('cp'))
#         trestbps = float(request.POST.get('trestbps'))
#         chol = float(request.POST.get('chol'))
#         fbs = float(request.POST.get('fbs'))
#         restecg = float(request.POST.get('restecg'))
#         thalach = float(request.POST.get('thalach'))
#         ca = float(request.POST.get('ca'))
#         thal = float(request.POST.get('thal'))
#         y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, ca, thal]])
        
        # print(y_pred)
        # if y_pred==1:
        #     y_pred='YES'
        #     print()
        
        # else:
        #     y_pred="NO"

    # return render(request, 'result.html', {'data': y_pred})   
    # return render(request, 'user.html', {'request': request})


# def result(request):
#     if request.method == 'POST':
#         try:
#             age = float(request.POST.get('age'))
#             sex = float(request.POST.get('sex'))
#             cp = float(request.POST.get('cp'))
#             trestbps = float(request.POST.get('trestbps'))
#             chol = float(request.POST.get('chol'))
#             fbs = float(request.POST.get('fbs'))
#             restecg = float(request.POST.get('restecg'))
#             thalach = float(request.POST.get('thalach'))
#             ca = float(request.POST.get('ca'))
#             thal = float(request.POST.get('thal'))
            
#             # Predict using your model
#             y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, ca, thal]])
#             if y_pred==1:
#                 y_pred='YES'
#                 print()
        
#             else:
#                 y_pred="NO"

    # return render(request, 'result.html', {'data': y_pred})  
    #         if y_pred == 1:
    #             result = 'YES'
    #         else:
    #             result = 'NO'
    #     except ValueError:
    #         # Handle input conversion errors here
    #         result = 'Invalid input'

    #     return render(request, 'result.html', {'data': result})
    # else:
    #     # Handle GET requests here
    #     return render(request, 'result.html')
