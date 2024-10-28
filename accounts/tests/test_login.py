import pytest
from django.urls import reverse
from model_bakery import baker

# from project.django_assertions import assert_contains, assert_not_contains


def test_user_not_found():
    ...


@pytest.fixture
def usuario(db, django_user_model):
    # Cria um usuário com email como identificador de login
    usuario_modelo = baker.make(
        django_user_model, email="testuser@example.com")
    senha = 'senha'
    usuario_modelo.set_password(senha)  # Configura a senha com hash
    usuario_modelo.save()
    # Armazena a senha em texto plano para usar no login
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


@pytest.mark.django_db
def test_login_page_status_200_ok(resp):
    # Verifica se a página de login está acessível com o status 200
    assert resp.status_code == 200


@pytest.fixture
def resp_post(client, usuario):
    # Realiza o login usando o email como identificador e a senha plana
    return client.post(reverse('login'), {'email': usuario.email, 'password': usuario.senha_plana})


@pytest.mark.django_db
def test_login_redirect(client, usuario, django_user_model):
    # Realiza o login com as credenciais do usuário
    response = client.post(reverse('login'), {
        'email': usuario.email,  # Usa o campo 'email' como identificador
        'password': usuario.senha_plana,
    })

    # Verifica se o status de resposta é de redirecionamento (302) após login
    assert response.status_code == 302
    # Verifica se o redirecionamento é para a URL correta (neste caso, 'home')
    assert response.url == reverse('home')
    # Confirma que o usuário foi criado e está presente no banco de dados
    assert django_user_model.objects.filter(email=usuario.email).exists()
