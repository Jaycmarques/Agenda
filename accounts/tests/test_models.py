from django.test import TestCase
from django.urls import reverse
from accounts.models import Category, Account
from django.contrib.auth import get_user_model


class AccountsModelTest(TestCase):

    def setUp(self):
        # Cria um usuário autenticado
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            password="testpass123"
        )  # type: ignore
        self.client.login(email="testuser@example.com", password="testpass123")

    def test_accounts_contact_creation_redirect_flow(self):
        # Criar a categoria necessária para o contato
        category = Category.objects.create(name='Amigos')

        # Fazer a requisição de criação do contato e verificar o redirecionamento
        response = self.client.post(reverse('create'), {
            'category': category.id,
            'first_name': 'Jay',
            'last_name': 'Marques',
            'phone': '5541885599663',
            'email': 'jay@email.com',
            'description': 'aaaadddddsdlkqowedkqow'
        })

        # Verificar se a resposta é um redirecionamento
        self.assertEqual(response.status_code, 302)

        # Extrair o ID do contato recém-criado
        # Captura o ID do contato que foi criado
        contact_id = Account.objects.latest('id').id

        # Verificar se o redirecionamento é para a página de detalhes do contato
        # Ajuste para esperar redirecionar para a página de atualização
        self.assertRedirects(response, reverse('update', args=[contact_id]))

        # Simular o update e redirecionar para a página de detalhes do contato
        response = self.client.post(reverse('update', args=[contact_id]), {
            'category': category.id,
            'first_name': 'Jay',
            'last_name': 'Marques',
            'phone': '5541885599663',
            'email': 'jay@email.com',
            'description': 'Descrição atualizada'
        })

        # Verificar se o redirecionamento final é para a página de detalhes do contato
        self.assertRedirects(response, reverse('contact', args=[contact_id]))

        # Fazer a requisição GET para a página de detalhes do contato
        response = self.client.get(reverse('contact', args=[contact_id]))
        # Verifica que a resposta é 200
        self.assertEqual(response.status_code, 200)
        self.assertIn('contact', response.context)
