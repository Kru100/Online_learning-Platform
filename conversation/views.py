from django.shortcuts import render, redirect
from .models import *
from instructor.models import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authent.views import *
from instructor.urls import *
from collections import defaultdict

@custom_login_required
def anounce_home(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        an = Anouncement.objects.filter(course=course_id).order_by('-time')
        course = Course.objects.get(id=course_id)
        context = {}
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if user.is_instructor == True:
            context = {'an': an, 'course': course, 'user': user}
        elif ta != None:
            context = {'an': an, 'course': course, 'ta': ta, 'new_notifications' : new_notifications}
        else:
            context = {'an': an, 'course': course, 'new_notifications' : new_notifications}
        return render(request, 'anouncement_home.html', context)
    except Exception as e:
        print(e)        

@custom_login_required
def make_announcement(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id)
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if user.is_instructor == True or ta != None:
            if request.method == 'POST':
                sender = request.session.get('email')
                anouncement = request.POST.get('anouncement')
                urls = request.POST.get('urls')
                an = Anouncement(sender=sender,urls=urls, anouncement=anouncement, course=course_id)
                an.save()
                messages.add_message(request, messages.INFO, 'Announcement Created successfully!!!')
                course = Course.objects.get(id=course_id)
                for user in course.enrolled.all():
                    Notifications.objects.create(student=user.id, course_id=course_id, text=f'New Notification in {course.name}')
                return redirect(reverse('annoucement', kwargs={'course_id': course_id}))
            return render(request, 'make-anouncement.html', {'user': user, 'ta': ta, 'new_notifications' : new_notifications})
        return redirect('error404/')
    except Exception as e:
        print(e)

@custom_login_required
def ask_doubt(request, course_id):
    try:
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if request.method == 'POST':
            email = request.session.get('email')
            doubt = request.POST.get('doubt')
            db = Doubt_ask(course_id=course_id, sender=email, doubt=doubt)
            db.save()
            n = Course.objects.get(id=course_id)
            user = User.objects.get(email=n.instructor)
            Notifications.objects.create(student=user.id, course_id=course_id, text=f'Someone had doubt in {n.name}')
            messages.add_message(request, messages.INFO,"Doubt Posted Successfully")
            return redirect(reverse('student-doubt', kwargs={'course_id': course_id}))
        course = Course.objects.get(id=course_id)
        return render(request,'ask-doubt.html', {'course': course, 'new_notifications': new_notifications})
    except Exception as e:
        print(e)

@custom_login_required
def reply_doubt(request, course_id, ask_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if user.is_instructor == True or ta.is_TA == True:
            if request.method == 'POST':
                email = request.session.get('email')            
                reply = request.POST.get('reply')
                dr = Doubt_ask.objects.get(id=ask_id)
                sender = dr.sender
                db = Doubt_replied(course_id=course_id, ask_id=ask_id, sender=sender, receiver=email,reply=reply)
                db.save()
                dbp = Doubt_replied.objects.get(ask_id = ask_id)
                dbs = Doubt_ask.objects.get(id=ask_id)
                dbs.is_replied = True
                dbs.reply_id = dbp.id
                dbs.save()
                messages.add_message(request, messages.INFO,"Replied Successfully")
                return redirect(reverse('instructor-doubt', kwargs={'course_id': course_id})) 
            return render(request,'reply.html', {'user': user, 'ta': ta, 'new_notifications': new_notifications})   
        return redirect('error404/')        
    except Exception as e:
        print(e)

@custom_login_required  
def doubtboard_instructor(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if user.is_instructor == True or ta != None:
            db = Doubt_ask.objects.filter(course_id=course_id).all()
            d = Doubt_replied.objects.filter(course_id=course_id).all()
            d_total = db.count()
            d_rep = d.count()
            d_not = d_total - d_rep
            sender_count = defaultdict(int)
            for i in d:
                sender_count[i.receiver] += 1
            print(sender_count)
            return render(request,'doubtboard_instructor.html', {'db': db, 'user': user, 'ta': ta, 'dt': d_rep, 'd': d_total, 'dn': d_not, 'sender_counts': sender_count.items(), 'new_notifications': new_notifications})
    except Exception as e:
        print(e)

@custom_login_required
def doubtboard_student(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if user.is_student == True:
            email = request.session.get('email')
            db = Doubt_ask.objects.filter(sender=email,course_id=course_id).all()
            dr = Doubt_replied.objects.filter(sender=email,course_id=course_id).all()
            return render(request, 'doubtboard_student.html', { 'db' : db, 'dr' : dr, 'new_notifications': new_notifications})
    except Exception as e:
        print(e)

@custom_login_required
def getHelp(request):
    try:
        notify = Notifications.objects.filter(student=user.id).all()
        new_notifications = False
        for n in notify:
          if n.is_viewed == False:
            new_notifications = True
            break
        if request.method == 'POST':
            email = request.session.get('email')
            helpline = request.POST.get('helpline')
            helps = Help(email=email, helpline=helpline)
            helps.save()
            messages.add_message(request, messages.INFO, 'Your Query is being sent successfully!!')
            return render(request, 'gethelp.html')
        return render(request, 'gethelp.html', { 'new_notifications': new_notifications})
    except Exception as e:
        print(e)

@custom_login_required
def make_Feedback(request, course_id):
    try:
        
        if request.method == 'POST':
            email = request.session.get('email')
            feedback = request.POST.get('feedback')
            fb = Feedback(email=email, feedback=feedback, course_id=course_id)
            fb.save()
            messages.add_message(request,messages.INFO, 'Thank you for your feedback!!!')
            return render(request, 'feedback.html')
        return render(request, 'feedback.html')
    except Exception as e:
        print(e)

@custom_login_required
def show_feedback(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            fb = Feedback.objects.filter(course_id=course_id)
            return render(request, 'show-feedback.html', {'fb':fb})
        return redirect('error/')
    except Exception as e:
        print(e)

def show_help(request):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_admin == True:
            hp = Help.objects.filter().all()
            return render(request, 'show-help.html', {'hp':hp})
        return redirect('error404/')
    except Exception as e:
        print(e)
        
def solve_query(request, id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_admin == True:
            hp = Help.objects.get(id=id)
            hp.delete()     
            messages.add_message(request, messages.INFO, "Query is solved!!")
            return redirect(reverse('show-help'))
        return redirect('/error404/')
    except Exception as e:
        print(e)
        
@custom_login_required
def notification_board(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        notify = Notifications.objects.filter(course_id=course_id, student=user.id)
        for n in notify:
            n.is_viewed = True
            n.save()
        return render(request,'notification_board.html',{'notify':notify})
    except Exception as e:
        print(e)
        
@custom_login_required
def notification(request):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        notify = Notifications.objects.filter(student=user.id).all().order_by('-id')
        notify_ids = [n.id for n in notify if not n.is_viewed]
        Notifications.objects.filter(id__in=notify_ids).update(is_viewed=True)
        context = {'notify': notify, 'user': user}
        # for n in notify:
        #     n.is_viewed = True
        #     n.save()
        return render(request,'notification.html',context)
    except Exception as e:
        print(e)