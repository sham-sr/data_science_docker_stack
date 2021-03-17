import setuptools

setuptools.setup(
    name="jupyter-flask_web-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/flask_web",
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
            'flask_web = jupyter_flask_web_proxy:setup_flask_web',
        ]
    },
    package_data={
        'jupyter_flask_web_proxy': ['icons/*'],
    },
)
