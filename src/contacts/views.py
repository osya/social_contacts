from django.views.generic import ListView

from contacts.models import Friend


class HomeView(ListView):
    def get_queryset(self):
        backend_name = self.kwargs.get('backend_name', None)
        if backend_name:
            social_user = self.request.user.social_auth.filter(
                provider=backend_name).first()
            if social_user:
                Friend.fetch(social_user, self.request)
                return Friend.objects.filter(
                    user_social_auth__id=social_user.id).order_by('name')
        return Friend.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['backend_name'] = self.kwargs.get('backend_name', None)
        return super(HomeView, self).get_context_data(object_list, **kwargs)
