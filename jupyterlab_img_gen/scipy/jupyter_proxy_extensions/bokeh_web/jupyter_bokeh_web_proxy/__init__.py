"""
Return config on servers to start for bokeh_web

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
from dotenv import load_dotenv

def setup_bokeh_web():
    def _bokeh_web_command(port,base_url):
        env_path=os.getenv("HOME")+"/work/dev_env/.env"
        load_dotenv(dotenv_path=env_path)
        work_app = os.getenv("BOKEH_APP")
        prefix = os.getenv("BOKEH_PREFIX")
        ws_origin = os.getenv("BOKEH_ALLOW_WS_ORIGIN")
        print('bokeh base_url: ', str(base_url))
        return ['bokeh', 'serve', work_app, '--port', str(port), '--allow-websocket-origin='+str(ws_origin), '--use-xheaders', '--prefix', '{base_url}'+prefix]
    return {
        'command': _bokeh_web_command,
        'environment': {},
        'absolute_url': True,
        'new_browser_tab': True,
        'timeout': 60,
        'launcher_entry': {
            'title': 'bokeh_web',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'bokeh_web.svg')
        }
    }