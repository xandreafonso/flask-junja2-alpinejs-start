from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    """Página inicial - demonstra o sistema de templates hierárquico"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard - exemplo de template de conteúdo herdando de layout"""
    # Dados de exemplo que seriam vindos do banco de dados
    dashboard_data = {
        'counter': 42,
        'message': 'Sistema funcionando perfeitamente!',
        'stats': {
            'users': 1250,
            'sales': 85300,
            'pending': 12,
            'activity': 87
        }
    }
    return render_template('pages/dashboard.html', **dashboard_data)

@app.route('/profile')
def profile():
    """Perfil do usuário - outro exemplo de template de conteúdo"""
    # Dados de exemplo do usuário
    user_data = {
        'user': {
            'name': 'João Silva',
            'email': 'joao@example.com',
            'phone': '(11) 99999-9999',
            'role': 'developer',
            'bio': 'Desenvolvedor Flask especializado em templates hierárquicos e sistemas escaláveis.',
            'join_date': 'Janeiro 2024'
        },
        'user_stats': {
            'posts': 42,
            'followers': 1250,
            'following': 380
        }
    }
    return render_template('pages/profile.html', **user_data)

@app.route('/ping')
def ping():
    """Endpoint de health check"""
    return 'pong'

@app.context_processor
def inject_template_vars():
    """Context processor para disponibilizar variáveis globalmente nos templates"""
    return {
        'app_name': 'Flask Hierarchical Templates',
        'version': '1.0.0',
        'year': 2024
    }

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
