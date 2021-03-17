import setuptools

setuptools.setup(
    name="jupyter-bokeh_web-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/bokeh_web",
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
            'bokeh_web = jupyter_bokeh_web_proxy:setup_bokeh_web',
        ]
    },
    package_data={
        'jupyter_bokeh_web_proxy': ['icons/*'],
    },
)
