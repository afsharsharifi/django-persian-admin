from django.views.generic import TemplateView


class LoginAdminView(TemplateView):
    template_name = "moonadmin/auth/login.html"
