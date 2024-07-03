from django.shortcuts import redirect, render
from app.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def Staff(request):
    var = staff.objects.all()
    return render(request,'Staff.html',{'var':var})

def add_staff(request):
    return render(request, 'Add_Staff.html')

def add_staff_save(request):
    if request.method == 'POST':
        s1 = request.POST['name']
        s2 = request.POST['s_id']
        s3 = request.POST['mobile']
        st = staff(name=s1,s_id=s2,Mobile=s3)
        st.save()
        msg_success = "Registered successfully, Refresh your Page"
        return render(request,'Add_Staff.html',{'msg_success':msg_success})
    else:
        return redirect('/')

def Customer(request):
    var = customer.objects.all()
    return render(request,'Customer.html',{'var':var})

def add_customer(request):
    return render(request,'Add_Customer.html')

def add_customer_save(request):
    if request.method == 'POST':
        c1 = request.POST['name']
        c2 = request.POST['c_id']
        c3 = request.POST['mobile']
        c4 = request.POST['area']
        ct = customer(c_name=c1,c_id=c2,Mobile=c3,area=c4)
        ct.save()
        msg_success = "Registered successfully, Refresh your Page"
        return render(request,'Add_Customer.html',{'msg_success':msg_success})
    else:
        return redirect('/')

def Deposit(request):
    var = record.objects.filter(Purpose='Deposit')
    return render(request,'Deposit.html',{'var':var})

def add_deposit(request):
    var = staff.objects.all()
    var1 = customer.objects.all()
    return render(request,'Add_Deposit.html',{'var':var,'var1':var1})

def add_deposit_save(request):
    if request.method == 'POST':
        d1 = request.POST['date']
        d2 = request.POST['sname']
        d3 = request.POST['cname']
        d4 = request.POST['amount']
        d5 = request.POST['status']
        d6 = request.POST['matter']
        d7 = request.POST['fdate']
        d8 = request.POST['purpose']
        dt = record(date=d1,s_name=d2,c_name=d3,amount=d4,status=d5,
                matter=d6,followup=d7,Purpose=d8)
        dt.save()
        msg_success = "Registered successfully, Refresh your Page"
        return render(request,'Add_Deposit.html',{'msg_success':msg_success})
    else:
        return redirect('/')

def Loan(request):
    var = record.objects.filter(Purpose='Loan')
    return render(request,'Loan.html',{'var':var})

def add_loan(request):
    var = staff.objects.all()
    var1 = customer.objects.all()
    return render(request,'Add_Loan.html',{'var':var,'var1':var1})

def add_loan_save(request):
    if request.method == 'POST':
        d1 = request.POST['date']
        d2 = request.POST['sname']
        d3 = request.POST['cname']
        d4 = request.POST['amount']
        d5 = request.POST['status']
        d6 = request.POST['matter']
        d7 = request.POST['fdate']
        d8 = request.POST['purpose']
        dt = record(date=d1,s_name=d2,c_name=d3,amount=d4,status=d5,
                matter=d6,followup=d7,Purpose=d8)
        dt.save()
        msg_success = "Registered successfully, Refresh your Page"
        return render(request,'Add_Loan.html',{'msg_success':msg_success})
    else:
        return redirect('/')

def report(request):
    var = record.objects.all()
    var1 = customer.objects.all()
    return render(request,'Report.html',{'var':var,'var1':var1})

def download(request,id):
    var =  record.objects.filter(id=id)
    var1 = customer.objects.all()
    return render(request,'Download.html',{'var':var,'var1':var1})