from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django import template
from django.template import loader
from django.template import Context,Template
from app.models import travelform
from django.core.mail import send_mail
import datetime
# Create your views here.
def index(request):
    destinations = []
    destinations = travelform.objects.all()
    for destination in destinations:
        print(destination.dname)
    return render(request, 'index.html', {'destinations': destinations})
def review(request):
    template = loader.get_template('review.html')
    if request.method == "POST":
        dname=request.POST['dname']
        rating=request.POST['rating']
        upd = travelform.objects.get(dname=dname)
        upd.count = upd.count+1
        upd.rating = str((float(upd.rating)+float(rating))/upd.count)
        upd.save()
        print("Data updated successfully")
    else:
        print("redirected")
    return render(request,'review.html')
def criticsedit(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        dimg = request.POST['dimg']
        rating = request.POST['rating']
        country = request.POST['country']
        ins = travelform(dname = dname,dimg = dimg,rating = rating,country = country)
        ins.save()
        print("Data saved successfully")
    return render(request,'critics.html')
def cities(request,cityname):
    destination = travelform.objects.get(dname=cityname)
    return render(request,'cities.html',{"destination":destination})
# def search(request):
#     if 'q' in request.GET:
#         message = 'you searched for : %r' % request.GET['q']
#     else:
#         message = 'you submitted an empty form.'
#     return HttpResponse("<html>%s</html" % message)
# def models_db1_delete(request):
#     if request.method  == "POST":
#         firstname = request.POST['fname']
#         dele = formcontact.objects.get(fname = firstname)
#         dele.delete()
#         print("Data deleted successfully")
#     else:
#         print("redirected")
#     return render(request,'index.html')
# def update(request):
#     print("the method is",request.method)
#     if request.method == "POST":
#         firstname=request.POST['fname']
#         newfirstname=request.POST['nfname']
#         upd = formcontact.objects.get(fname=firstname)
#         upd.fname = newfirstname
#         upd.save()
#         print("Data updated successfully")
#     else:
#         print("redirected")
#     return render(request,'index.html')
# def newMethod(request):
#     return HttpResponse('newMethod')
# def currentDate(request):
#     now = datetime.datetime.now() + datetime.timedelta(hours = 1)
#     html = '<html><body>time is %s</body></html>' %now
#     return HttpResponse(html)
# def one_hour_ahead(request):
#     dt = datetime.now() + datetime.timedelta(hours=1)
#     html = "<html><body style='text-align:center';>It %s hour(s), it will be %s</body></html>" % (1, dt)
#     return HttpResponse(html)
# def hour_ahead(request,offset):
#     try:
#         offset=int(offset)
#     except ValueError:
#         raise Http404 ()
#     dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
#     ht="<html><body>in %s hours, the time will be %s.</body></html>"%(offset,dt)
#     return HttpResponse(ht)
# def templateview(request):
#     template  = loader.get_template('index.html')
#     return HttpResponse(template.render())
# def index2view(request):
#     template = loader.get_template('index.html')
#     name={
#         'student':'sanjith',
#     } 
#     return HttpResponse(template.render(name))
# def test2(request):
#     t=Template('my name is {{ name }}')
#     c=Context({'name':'defg'})
#     return HttpResponse(t.render(c))
# def test3(request):
#     template=loader.get_template('order.html')
#     name ={
#         'person_name':'sanjith',
#         'company':'ABC',
#         'ship_date':datetime.datetime.now(),
#         'item_list':[10,20],
#         'ordered_warranty':10,
#     }
#     return HttpResponse(template.render(name))
# def context(request):
#     person={'name':'ranjith','age':'20'}
#     t=Template('{{person.name}} is {{person.age}} years')
#     c=Context({'person':person})
#     html=t.render(c)
#     return HttpResponse(html)
# def tags(request):
#     template=loader.get_template('tags.html')
#     name={}
#     name["key1"] = [1,2]
#     return HttpResponse(template.render(name))
# def forloop(request):
#     template=loader.get_template('loop.html')
#     list={
#         'a':[1,2],
#         'name':['a','b','c']
#     }
#     return HttpResponse(template.render(list))

# def block(request):
#     template = loader.get_template('current_datetime.html')
#     name = {
#         "block title" : "My Bio",
#         'block content' : 'I am sanjith I am pursuing BE CSE 3rd Year in Kongu Engineering College',
#         'block footer' : 'That all about me',
#         'name' : 'sanjith'
#     }
#     return HttpResponse(template.render(name))
# def pathsecure(request):
#     return HttpResponse("welcome to the page at %s" % request.is_secure())
# def good(request):
#     try:
#         ua = request.META['HTTP_USER_AGENT']
#     except KeyError:
#         ua = 'unknown'
#     return HttpResponse("your broswer is %s" % ua)
# def display_meta(request):
#     values = request.META.items()
    
#     html=[]
#     for k,v in values:
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))

# def search_form(request):
#     return render(request,'search.html')


# def contact(request):
#     errors=[]
#     if request.method=="POST":
#         if not request.POST.get('subject',''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message',''):
#             errors.append('Enter a message.')
#         if not request.POST.get('email',''):
#             errors.append('mail cannot be empty.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email','praneshvr.19cse@kongu.edu.com'),
#                 ['nandhakumarrg.19cse@kongu.edu'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request,'contactform.html',{
#         'errors':errors,
#         'subject':request.POST.get('subject',''),
#         'message':request.POST.get('message',''),
#         'email':request.POST.get('email',''),
#     })

