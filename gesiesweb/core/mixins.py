from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

from braces.views import LoginRequiredMixin


class LoginRequerido(LoginRequiredMixin):

    pass


class ResponsableRequiredMixin(LoginRequiredMixin):
    """
    Mixin allows you to require a user with `es_responsable` set to True.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.session['es_responsable']:  # If the user is a standard user,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.get_login_url(),
                                         self.get_redirect_field_name())

        return super(ResponsableRequiredMixin, self).dispatch(
            request, *args, **kwargs)