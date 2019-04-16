# some_app/views.py
from django.views.generic import TemplateView, ListView, DetailView
from developments.models import Development, Type
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class HomeView(ListView):
    template_name = "index.html"
    model = Development

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_featured=True).order_by('?')
        return qs

    def post(self, *args, **kwargs):
        self.object = self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        # mail
        send_contact_mail(self.request)
        return self.render_to_response(context)    


class ProjectListView(ListView):
    template_name = "listado.html"
    model = Development

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "filter_types": set(Type.objects.all().filter(development__isnull=False))})
        return context


class ProjectDetailView(DetailView):
    template_name = "detalle_desarrollo.html"
    slug_url_kwarg = 'project_slug'
    model = Development

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        # mail
        send_contact_mail(self.request)
        return self.render_to_response(context)

def send_contact_mail(request):
    mail = EmailMultiAlternatives(
          subject="Contacto de Gamarq Web",
          body=request.POST["txtMsg"],
          from_email=request.POST["txtEmail"],
          to=["mcattan@gamarq.com.mx"],
          headers={"Reply-To": "mcattan@gamarq.com.mx"}
        )

    mail.send()

    
