import msgraph
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from msgraph import Contact

from contacts.msgraph.email_addresses_collection import EmailAddressesCollectionPage


class HomeView(TemplateView):
    """
        HomeView based on TemplateView
    """
    template_name = 'contacts/home.html'

    def get_context_data(self, **kwargs):
        super(HomeView, self).get_context_data(**kwargs)
        kwargs['signin_url'] = settings.MSGRAPH_AUTH_PROVIDER.get_auth_url(
            self.request.build_absolute_uri(reverse('contacts:msgraph_authorized')))

        if settings.MSGRAPH_AUTH_PROVIDER.access_token:
            client = msgraph.GraphServiceClient(
                settings.MSGRAPH_BASE_URL,
                settings.MSGRAPH_AUTH_PROVIDER,
                settings.MSGRAPH_HTTP_PROVIDER)

            # Fix Contact.email_addresses property
            def email_addresses(self_):
                """Gets and sets the emailAddresses

                        Returns:
                            :class:`EmailAddressesCollectionPage<microsoft.graph.request.email_addresses_collection.EmailAddressesCollectionPage>`:
                                The emailAddresses
                        """
                if 'emailAddresses' in self_._prop_dict:
                    return EmailAddressesCollectionPage(self_._prop_dict['emailAddresses'])
                else:
                    return None

            Contact.email_addresses = property(email_addresses)

            # TODO: Add paging for MSGraph Contacts. Currently only fixed number of contacts requested
            kwargs['msgraph_contacts'] = client.me.contacts. \
                request(top=100, select='displayName,emailAddresses', order_by='displayName', skip=100).get()
        return kwargs


def msgraph_authorized(request):
    settings.MSGRAPH_AUTH_PROVIDER.authenticate(
        request.GET['code'],
        request.build_absolute_uri(reverse('contacts:msgraph_authorized')),
        settings.MSGRAPH_CLIENT_SECRET)
    return HttpResponseRedirect(reverse('contacts:home'))
