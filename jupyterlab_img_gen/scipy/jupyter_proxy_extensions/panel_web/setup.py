import setuptools

setuptools.setup(
    name="jupyter-panel_web-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/panel_web",
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
            'panel_web = jupyter_panel_web_proxy:setup_panel_web',
        ]
    },
    package_data={
        'jupyter_panel_web_proxy': ['icons/*'],
    },
)
