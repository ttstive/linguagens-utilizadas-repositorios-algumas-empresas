import requests
import pandas as pd
from dados_repos import requisicoes_request

apple_repos = requisicoes_request('apple')
ling_utilizadas_apple = apple_repos.cria_dataframe()
ling_utilizadas_apple.to_csv('dados/linguagens_apple.csv')

