from urllib import request
import requests as req


class Redash:
    class Query:
        def __init__(self, api_url: str):
            """

            Args:
                api_url (str) : api endpoint
            """
            self.url = request.urljoin(api_url, 'queries/')

        def download_query_results(
                self,
                query_id: str,
                api_key: str,
                filename: str = 'results.csv') -> None:
            """

            Args:
                query_id (str) : specific query id
                api_key (str) : api authorization key
                filename (str) : output file name

            Returns:

            """

            opener = request.build_opener()
            opener.addheaders = [('Authorization', f'Key {api_key}')]
            request.install_opener(opener=opener)

            url = request.urljoin(self.url, f'{query_id}/')
            url = request.urljoin(url, 'results.csv')
            request.urlretrieve(url=url, filename=filename)