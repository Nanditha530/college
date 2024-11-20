from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def adminhome(request):
    return render(request,'adminhome.html')

def mainhome(request):
    return render(request,'mainhome.html')
def index(request):
    return render(request,'index.html')

def dep_add(request):
    if request.method=="POST":
        d=request.POST['dep']
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse("success")
    else:
        return render(request,'dep_add.html')




def reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='teacher')
        x.save()
        y=Teacher.objects.create(Tid=x,Depid_id=d,Age=a,Address=ad,Qulification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
    return render(request,'reg_teacher.html',{'x1':x})




def reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='student',is_active=False)
        x.save()
        y=Student.objects.create(Depid_id=d,Sid=x,Age=a,Address=ad)
        y.save()
        return HttpResponse("student registered")
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})
    


def viewstudent(request):
    x=Student.objects.all()
    return render(request,'viewstudent.html',{'x1':x})

def deleteteacher(request,uid):
    x=User.objects.get(id=uid)
    x.delete()
    return redirect(viewteacher)





def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.Sid.is_active=True
    st.Sid.save()
    return redirect(viewstudent)


def studenthome(request):
    return render(request,'studenthome.html')

def teacherhome(request):
    return render(request,'teacherhome.html')


def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=='teacher':
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=='student' and user.is_active==1:
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse("not valid")
    else:
        return render(request,'logins.html')
    


def approved_stview(request):
    x=User.objects.filter(is_active=1,usertype="student")
    return render(request,'approved_stview.html',{'x':x})

def approved_teaview(request):
    x=User.objects.filter(is_active=1,usertype="teacher")
    return render(request,'approved_teaview.html',{'x':x})


        
  


def updatest(request):
    stud=request.session.get('stud_id')
    stu=Student.objects.get(Sid_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':stu,'data':user})

def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        Sid=stud.Sid_id
        user=User.objects.get(id=Sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("success")
    

def updateteach(request):
    teach=request.session.get('teach_id')
    x=Teacher.objects.get(Tid_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updateteacher.html',{'view':x,'data':user})

def updateteacher(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.Tid_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        teach.Age=request.POST['age']
        teach.Address=request.POST['address']
        teach.save()
        return HttpResponse("success")
    else:
        return render (request,'teacherhome.html')
    
def lgout(request):
    logout(request)
    return redirect(logins)




def viewteacher(request):
    x=Teacher.objects.all()
    return render(request,'viewteacher.html',{'x1':x})

def approved(request):
    user=User.objects.filter(is_active=1,usertype='student')

    return render(request,'view_teach.html',{'x1':user})


def deletestudent(request,uid):
    x=User.objects.get(id=uid)
    x.delete()
    return redirect(viewstudent)



def depbystudent(request):
    teacher=Teacher.objects.get(Tid=request.user)
    department_student=Student.objects.filter(Depid=teacher.Depid)
    
    return render(request,'department_student.html',{'x1':department_student})



def depbyteacher(request):
    student=Student.objects.get(Sid=request.user)
    department_teacher =Teacher.objects.filter(Depid=student.Depid)
    

    return render(request,'department_teacher.html',{'x1':department_teacher})



