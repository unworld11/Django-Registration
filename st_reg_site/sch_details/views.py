from django.shortcuts import render
import csv

# Create your views here.

def details(request):
    return render(request,'strdetails.html')

def studata(request):
    if request.method == 'POST':
        dict1 = request.POST
        with open('studata.csv','a') as csvfile:
            wrt = csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    return render(request,'strchoice.html')

