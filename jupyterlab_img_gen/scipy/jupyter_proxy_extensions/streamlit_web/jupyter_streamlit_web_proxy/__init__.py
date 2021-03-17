"""
Return config on servers to start for streamlit_web

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
from dotenv import load_dotenv

def setup_streamlit_web():
    def _streamlit_web_command(port):
        env_path=os.getenv("HOME")+"/work/dev_env/.env"
        load_dotenv(dotenv_path=env_path)
        work_app = os.getenv("STREAMLIT_APP")
        print('streamlit app path: ', work_app)
        return ['streamlit', 'run', work_app, '--server.port', str(port)]
    return {
        'command': _streamlit_web_command,
        'environment': {},
        'timeout': 120,
        'launcher_entry': {
            'title': 'streamlit_web',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'streamlit_web.svg')
        }
    }