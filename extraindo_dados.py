import requests
import pandas as pd
from dados_repos import requisicoes_request


## Agora devemos estanciar (executar nossa classe)
amazon_repositorios = requisicoes_request('amzn')
ling_mais_utilizadas_amzn = amazon_repositorios.cria_dataframe()
#print(ling_mais_utilizadas_amzn)

netflix_repositorios = requisicoes_request('netflix')
ling_mais_utilizadas_netflix = netflix_repositorios.cria_dataframe()

spotify_repositorios = requisicoes_request('spotify')
ling_mais_utilizadas_sporify = spotify_repositorios.cria_dataframe()

# agora vamos salvar os dataframes que serão criados

ling_mais_utilizadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_utilizadas_sporify.to_csv('dados/linguagens_spotify.csv')
ling_mais_utilizadas_netflix.to_csv('dados/linguagens_netflix.csv')

apple_repo = requisicoes_request('apple')
ling_utilizadas = apple_repo.cria_dataframe()
ling_utilizadas.to_csv('dados/linguagens_apple.csv')