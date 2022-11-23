from .interface import CheckUrlClientInterface


class CheckUrlClient(CheckUrlClientInterface):
    def __init__(self, client, url_list: list):
        self.client = client
        self.url_list = url_list

    def _add_index_on_url_list(self):
        return [(index, item) for index, item in enumerate(self.url_list)]

    def _check_url(self, url: str):
        response = self.client.get(url)
        return response.status_code

    def run(self):
        url_list = self._add_index_on_url_list()
        urls_verified_list = list()

        for url_information in url_list:
            index = url_information[0]
            url = url_information[1]
            status_code = self._check_url(url)

            data = {
                "index": index,
                "url": url,
                "status_code": status_code,
            }

            urls_verified_list.append(data)

        return urls_verified_list
