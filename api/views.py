from django.http import HttpResponse
from .email_utils import send_custom_email
from django.views.generic import View

class SendFormEmail(View):
    def get(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        zipcode = request.GET.get('zipcode', None)
        email = request.GET.get('email', None)
        address = request.GET.get('address', None)
        phone = request.GET.get('phone', None)
        age = request.GET.get('age', None)

        data = "First Name: "+first_name+"\n Last Name: "+last_name+"\n Zipcode: "+zipcode+"\n Email: "+email+"\n Address: "+address+"\n Phone: "+phone+"\n Age: "+age;
        # """.format(first_name,last_name,email,address,phone);

        # print(data);
        subject = 'Chris Property: New Application'
        message = data;
        recipient_list = ['ganiuibrahim3000@gmail.com']  # Replace with the recipient's email addresses

        send_custom_email(subject, message, recipient_list)

        return HttpResponse("Email Send Successfully!");
