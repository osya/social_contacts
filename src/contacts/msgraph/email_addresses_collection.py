#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import json

from msgraph import EmailAddress
from msgraph.collection_base import CollectionPageBase, CollectionRequestBase, CollectionResponseBase


class EmailAddressesCollectionRequest(CollectionRequestBase):
    def __init__(self, request_url, client, options):
        """Initialize the EmailAddressesCollectionRequest

        Args:
            request_url (str): The url to perform the EmailAddressesCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EmailAddressesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EmailAddressesCollectionPage

        Returns:
            :class:`EmailAddressesCollectionPage<msgraph.request.email_addresses_collection.EmailAddressesCollectionPage>`:
                The EmailAddressesCollectionPage
        """
        self.method = 'GET'
        collection_response = EmailAddressesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the EmailAddressesCollectionPage in async

        Fields:
            :class:`EmailAddressesCollectionPage<msgraph.request.email_addresses_collection.EmailAddressesCollectionPage>`:
                The EmailAddressesCollectionPage
        """
        future = self._client._loop.run_in_executor(None, self.get)
        collection_page = yield from future
        return collection_page


class EmailAddressesCollectionResponse(CollectionResponseBase):
    @property
    def collection_page(self):
        """The collection page stored in the response JSON

        Returns:
            :class:`EmailAddressesCollectionPage<msgraph.request.email_addresses_collection.EmailAddressesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict['value']
        else:
            self._collection_page = EmailAddressesCollectionPage(self._prop_dict['value'])

        return self._collection_page


class EmailAddressesCollectionPage(CollectionPageBase):
    def __getitem__(self, index):
        """Get the EmailAddress at the index specified

        Args:
            index (int): The index of the item to get from the EmailAddressesCollectionPage

        Returns:
            :class:`EmailAddress<msgraph.model.email_address.EmailAddress>`:
                The EmailAddress at the index
        """
        return EmailAddress(self._prop_list[index])

    def email_addresses(self):
        """Get a generator of EmailAddress within the EmailAddressesCollectionPage

        Yields:
            :class:`EmailAddress<msgraph.model.email_address.EmailAddress>`:
                The next Attachment in the collection
        """
        for item in self._prop_list:
            yield EmailAddress(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EmailAddressesCollectionPage

        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = EmailAddressesCollectionRequest(next_page_link, client, options)
