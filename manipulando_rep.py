import requests
import base64

class importar_dados_git:
    def __init__(self, username):
       self.username = username
       self.api_base = 'https://api.github.com'
       token_acess = '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'
       self.headers = {'Authorization': 'Bearer ' + token_acess,
                       'X-GitHub-Api-Version': '2022-11-28'}
       
    def cria_repositorio (self, nome_repositorio): # vamos criar um dicionario, com nome, descrição e status
        dados_repositorio = {
            'name': nome_repositorio,
            'description': 'Dados de repositórios de algumas empresas',
            'private': False
        }

        response = requests.post(f'{self.api_base}/user/repos',
                                 json = dados_repositorio, headers= self.headers)
        print("status da criação do repositório: {}".format(response.status_code))

# aqui vamos criar um metodo que vai configurar os nossos arquivos que vão para o git, passaremos o nome_repo, nome_arquivo e o caminho_arquivo
   
    def configure_path(self, nome_repositorio, nome_arquivo, caminho_arquivo):
       with open(caminho_arquivo, 'rb') as file:
           file_content = file.read()

           file_encoded = base64.b64encode(file_content)

    #temos que realizar o uplodad
           url = f'{self.api_base}/repos/{self.username}/{nome_repositorio}/contents/{nome_arquivo}'
           dados_repositorio = {
               'message': 'Adicionar novo arquivo OK',
               'content': file_encoded.decode('utf-8')
           }
           response = requests.put(url, json = dados_repositorio, headers = self.headers)
           print("status da criacao do repositorio: {}".format(response.status_code))


