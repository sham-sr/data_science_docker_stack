import setuptools

setuptools.setup(
    name="jupyter-vscode_web-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/vscode_web",
    author="sham-sr",
    description="shamsr.rus@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'vscode_web = jupyter_vscode_web_proxy:setup_vscode_web',
        ]
    },
    package_data={
        'jupyter_vscode_web_proxy': ['icons/*'],
    },
)
