"""
Return config on servers to start for flask_web

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
from dotenv import load_dotenv

def setup_flask_web():
    def _flask_web_command(port):
        env_path=os.getenv("HOME")+"/work/dev_env/.env"
        load_dotenv(dotenv_path=env_path)
        work_app = os.getenv("FLASK_APP")
        print('flask app path: ', work_app)
        return ['flask', 'run','--port', str(port)]
    return {
        'command': _flask_web_command,
        'environment': {},
		'timeout': 20,
        'launcher_entry': {
            'title': 'flask_web',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'flask_web.svg')
        }
    }
