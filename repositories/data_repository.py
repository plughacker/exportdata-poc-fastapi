from typing import Any, List, Dict
import requests


class DataRepository:

    def get_transactions_data(self, *args, **kwargs) -> List[Dict[str, Any]]:
        url = 'https://api.dev.plugpagamentos.com/v1/search'
        try:
            response = requests.post(url, headers=self.__get_headers(), json=self.__get_body())
            return response.json()['data']['allTransactionDocuments']['edges']
        except Exception as e:
            print('Loggin excepiton', e)
        return []


    def __get_headers(self, *args, **kwargs):
        return {
            'X-Client-Id': '523afbe7-36dc-4654-9dba-e7167d0e5e2d',
            'X-Api-Key': 'ca7a396f-ea5c-4771-9df3-bfd1013f2df8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Connection': 'keep-alive',
        }

    def __get_body(self, *args, **kwargs) -> Dict[str, str]:
        body = ''' {
            allTransactionDocuments{
                edges {
                    node {
                        id
                        clientId
                        createdAt
                        amount
                        originalAmount
                        description
                        status
                        updatedAt
                    }
                }
            }
        }'''
        return {'query': body}