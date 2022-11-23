from abc import ABC


class CheckUrlClientInterface(ABC):
    def _add_index_on_url_list(self):
        pass

    def _check_url(self, url: str):
        pass

    def run(self):
        pass
