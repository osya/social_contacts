import facebook
import msgraph
from django.conf import settings
from django.db import models
from social_django.models import UserSocialAuth
from social_django.utils import load_strategy

from contacts.msgraph.auth_provider import AuthProvider


class Friend(models.Model):
    # social_id is not a PositiveInteger, because in Microsoft Graph id_ field has string type
    social_id = models.CharField(max_length=100, unique=True, default=0, db_index=True)
    name = models.CharField(max_length=100)
    user_social_auth = models.ForeignKey(UserSocialAuth, related_name='friends', default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def fetch(social_user, request):
        if not social_user or social_user.provider not in ('facebook', 'microsoft-graph'):
            return

        if social_user.provider == 'facebook':
            graph = facebook.GraphAPI(social_user.access_token)
            user = graph.get_object('me')
            friends = graph.get_connections(user['id'], 'friends').get('data')

            for friend in friends:
                if not Friend.objects.filter(social_id=friend.get('id')).exists():
                    Friend(
                        social_id=friend.get('id'),
                        name=friend.get('name'),
                        user_social_auth=social_user
                    ).save()
        elif social_user.provider == 'microsoft-graph':
            backend = social_user.get_backend_instance(load_strategy(request))
            auth_provider = AuthProvider(
                http_provider=settings.MSGRAPH_HTTP_PROVIDER,
                client_id=settings.SOCIAL_AUTH_MICROSOFT_GRAPH_KEY,
                scopes=settings.MSGRAPH_SCOPES,
                token_type=social_user.extra_data.get('token_type'),
                expires_in=social_user.extra_data.get('expires'),
                access_token=social_user.access_token,
                refresh_token=social_user.extra_data.get('refresh_token'),
                redirect_uri=backend.get_redirect_uri(),
                client_secret=settings.SOCIAL_AUTH_MICROSOFT_GRAPH_SECRET,
                auth_server_url='{0}{1}'.format(settings.MSGRAPH_AUTHORITY, '/common/oauth2/v2.0/authorize'),
                auth_token_url='{0}{1}'.format(settings.MSGRAPH_AUTHORITY, '/common/oauth2/v2.0/token')
            )
            client = msgraph.GraphServiceClient(
                settings.MSGRAPH_BASE_URL,
                auth_provider,
                settings.MSGRAPH_HTTP_PROVIDER
            )
            # TODO: Add paging for MSGraph Contacts. Currently only fixed number of contacts requested
            friends = client.me.contacts. \
                request(top=100, select='displayName,emailAddresses', order_by='displayName', skip=100).get()
            for friend in friends:
                if not Friend.objects.filter(social_id=friend.id_).exists():
                    Friend(
                        social_id=friend.id_,
                        name=friend.display_name,
                        user_social_auth=social_user
                    ).save()
