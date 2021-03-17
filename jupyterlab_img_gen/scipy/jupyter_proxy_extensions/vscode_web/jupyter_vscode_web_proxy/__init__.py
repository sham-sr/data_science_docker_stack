"""
Return config on servers to start for vscode_web

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.htmlS
for more information.
"""
import os
from dotenv import load_dotenv

def setup_vscode_web():
    def _vscode_web_command(port):
        env_path=os.getenv("HOME")+"/work/dev_env/.env"
        load_dotenv(dotenv_path=env_path)
        working_dir = os.getenv("CODE_WORKDIR")
        print('vscode working dir set: ', working_dir)
        return ['code-server','--auth','none','--disable-telemetry','--port=' + str(port), working_dir]
    return {
        'command': _vscode_web_command,
        'environment': {},
        'timeout': 120,
        'launcher_entry': {
            'title': 'vscode_web',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'vscode_web.svg')
        }
    }