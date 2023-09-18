import requests
import pandas as pd
from manipulando_rep import importar_dados_git

novo_repositorio = importar_dados_git('ttstive')

# criar novo repositorio

nome_repo = 'linguagens-utilizadas-repositorios-algumas-empresas'
novo_repositorio.cria_repositorio(nome_repo)

novo_repositorio.configure_path(nome_repo, 'linguagens_amazon.csv', 'dados/linguagens_amzn.csv')
novo_repositorio.configure_path(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repositorio.configure_path(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repositorio.configure_path(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')