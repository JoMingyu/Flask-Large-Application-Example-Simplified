import ujson
from unittest import TestCase as TC

from app import app


class TCBase(TC):
    def __init__(self, *args, **kwargs):
        TC.__init__(self, *args, **kwargs)

        self.client = app.test_client()

    def _create_fake_account(self):
        pass

    def _get_tokens(self):
        self.access_token = None
        self.refresh_token = None

    def setUp(self):
        self._create_fake_account()
        self._get_tokens()

    def tearDown(self):
        pass

    def json_request(self, method, target_url_rule, data, token=None, *args, **kwargs):
        """
        Helper for json request

        :param method: Request method
        :type method: func

        :param target_url_rule: URL rule for request
        :type target_url_rule: str

        :param data: JSON payload for request body
        :type data: dict or list

        :param token: JWT or OAuth's access token with prefix(Bearer, JWT, ...). if token is None, use self.access_token
        :type token: str

        :return: response
        """
        if token is None:
            token = self.access_token

        return method(
            target_url_rule,
            data=ujson.dumps(data),
            content_type='application/json',
            headers={'Authorization': token},
            *args,
            **kwargs
        )

    def request(self, method, target_url_rule, data=None, token=None, *args, **kwargs):
        if token is None:
            token = self.access_token

        return method(
            target_url_rule,
            data=data,
            headers={'Authorization': token},
            *args,
            **kwargs
        )

    def get_response_data(self, resp):
        return ujson.loads(resp.data.decode())
