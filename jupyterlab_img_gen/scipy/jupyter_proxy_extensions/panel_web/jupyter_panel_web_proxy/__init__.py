"""
Return config on servers to start for panel_web

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
from dotenv import load_dotenv

def setup_panel_web():
    def _panel_web_command(port):
        env_path=os.getenv("HOME")+"/work/dev_env/.env"
        load_dotenv(dotenv_path=env_path)
        work_app = os.getenv("PANEL_APP")
        prefix = os.getenv("PANEL_PREFIX")
        ws_origin = os.getenv("PANEL_ALLOW_WS_ORIGIN")
        print('panel app path: ', work_app)
        return ['panel', 'serve', work_app, '--port='+str(port), '--use-xheaders', '--prefix', '{base_url}'+prefix, '--allow-websocket-origin='+str(ws_origin)]
    return {
        'command': _panel_web_command,
        'environment': {},
        'absolute_url': True,
        'new_browser_tab': True,
        'timeout': 60,
        'launcher_entry': {
            'title': 'panel_web',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'panel_web.svg')
        }
    }
