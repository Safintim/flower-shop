import phonenumbers
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from core.models import Callback


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler403(request, exception):
    return render(request, '403.html', status=403)


class AboutTemplateView(generic.TemplateView):
    template_name = 'about.html'


class ShippingAndPaymentTemplateView(generic.TemplateView):
    template_name = 'shipping_and_payment.html'


class ContactsTemplateView(generic.TemplateView):
    template_name = 'contacts.html'


class CallbackView(generic.View):
    def post(self, request, *args, **kwargs):
        phone = request.POST.get('phone')
        try:
            phone_parse = phonenumbers.parse(phone, settings.PHONENUMBER_DEFAULT_REGION)
            if phonenumbers.is_valid_number(phone_parse):
                Callback.objects.create(phone=phone)
                return JsonResponse({'status': 'ok'})
        except phonenumbers.phonenumberutil.NumberParseException:
            pass
        return JsonResponse({'status': 'error'})
