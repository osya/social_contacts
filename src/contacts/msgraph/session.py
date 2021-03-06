from __future__ import unicode_literals

from time import time

from msgraph.session_base import SessionBase


class Session(SessionBase):
    def __init__(self,
                 token_type,
                 expires_in,
                 scope_string,
                 access_token,
                 client_id,
                 auth_server_url,
                 redirect_uri,
                 refresh_token=None,
                 client_secret=None):
        self.token_type = token_type
        self._expires_at = time() + int(expires_in)
        self.scope = scope_string.split(' ')
        self.access_token = access_token
        self.client_id = client_id
        self.auth_server_url = auth_server_url
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token
        self.client_secret = client_secret

    def is_expired(self):
        """Whether or not the session has expired

        Returns:
            bool: True if the session has expired, otherwise false
        """
        # Add a 10 second buffer in case the token is just about to expire
        return self._expires_at < time() - 10

    def refresh_session(self, expires_in, scope_string, access_token, refresh_token):
        self._expires_at = time() + int(expires_in)
        self.scope = scope_string.split(' ')
        self.access_token = access_token
        self.refresh_token = refresh_token

    def save_session(self, **save_session_kwargs):
        """Save the current session.
        IMPORTANT: This implementation should only be used for debugging.
        For real applications, the Session object should be subclassed and
        both save_session() and load_session() should be overwritten using
        the client system's correct mechanism (keychain, database, etc.).
        Remember, the access_token should be treated the same as a password.

        Args:
            save_session_kwargs (dicr): To be used by implementation
            of save_session, however save_session wants to use them. The
            default implementation (this one) takes a relative or absolute
            file path for pickle save location, under the name "path"
        """
        path = 'session.pickle'
        if 'path' in save_session_kwargs:
            path = save_session_kwargs['path']

        with open(path, 'wb+') as session_file:
            import pickle
            # pickle.HIGHEST_PROTOCOL is binary format. Good perf.
            pickle.dump(self, session_file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_session(**load_session_kwargs):
        """Save the current session.
        IMPORTANT: This implementation should only be used for debugging.
        For real applications, the Session object should be subclassed and
        both save_session() and load_session() should be overwritten using
        the client system's correct mechanism (keychain, database, etc.).
        Remember, the access_token should be treated the same as a password.

        Args:
            load_session_kwargs (dict): To be used by implementation
            of load_session, however load_session wants to use them. The
            default implementation (this one) takes a relative or absolute
            file path for pickle save location, under the name "path"

        Returns:
            :class:`Session`: The loaded session
        """
        path = 'session.pickle'
        if 'path' in load_session_kwargs:
            path = load_session_kwargs['path']

        with open(path, 'rb') as session_file:
            import pickle
            return pickle.load(session_file)
