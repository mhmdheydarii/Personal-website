from django.views.generic import ListView, FormView, TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project
from .forms import ContactForm


# Create your views here.

class IndexView(SuccessMessageMixin, TemplateView):

    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        context["form"] = ContactForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(self.request, "پیام شما با موفقیت ارسال شد")
            return redirect("portfolio:index")
        else:
            messages.error(self.request, "پیام شما ارسال نشد مجدادا تلاش کنید")
        
        context = self.get_context_data()
        context["form"] = form

        return self.render_to_response(context)

    



    
