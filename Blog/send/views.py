from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from send.models import Mail
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index1(request):
    send_mail('SUBJECT',
        'BODY',
        'klausmikelsonoriginal@gmail.com',
        ['1arshanahmad@gmail.com'],
        fail_silently=False)
    return render(request,'send/send.html')

def index2(request):
    SUBJECT =request.POST.get('subject')
    BODY =request.POST.get('body')
    from_email =request.POST.get('from_email')
    to_email =request.POST.get('to_email')
    sent_file =request.FILES.get('sent_file')

    email =EmailMessage(
        SUBJECT ,
        BODY ,
        from_email,
        [to_email] ,
        #attachments= sent_file,

    )

    email.attach_file(sent_file)
    email.send()
    return render(request,'send/send1.html')
        
class mailing(CreateView):        
    model =Mail
    fields =['subject','body','from_email','to_email','sent_file']
    template_name = 'send/send.html'



"""class index2(generic.ListView):
    model = ,Blogs1
    template_name ='blog/search.html'
    def get_queryset(self):
        query =self.request.GET.get('q') 
        object_list1 =Blogs.objects.filter(
            Q(author__username__icontains=query) )
        object_list2 =Blogs1.objects.filter(Q(blog_content__icontains=query))
        object_list =sorted(chain
        (object_list1,object_list2),
        key =lambda instance: instance.pk,reverse =True)
                
        return object_list
"""


