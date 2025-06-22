import requests # aqui importamos a biblioteca requests

BASE_URL = "https://jsonplaceholder.typicode.com" # URL base da API JSONPlaceholder

def test_get_users_status_code(): # função para testar o status code da requisição
    response = requests.get(f"{BASE_URL}/users") # faz uma requisição GET para a rota /users
    assert response.status_code == 200 # verifica se o status code é 200 (OK)

def test_get_users_count(): # função para testar a contagem de usuários 
    response = requests.get(f"{BASE_URL}/users") # faz uma requisição GET para a rota /users
    assert response.status_code == 200 # verifica se o status code é 200 (OK) 
    data = response.json() # converte a resposta JSON em um objeto Python
    assert isinstance(data, list)  # verifica se o dado retornado é uma lista
    assert len(data) > 0  # verifica se a lista não está vazia
    assert len(data) == 10  # JSONPlaceholder sempre retorna 10 usuários
