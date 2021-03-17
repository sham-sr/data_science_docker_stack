import setuptools

setuptools.setup(
    name="jupyter-streamlit_web-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/streamlit_web",
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
            'streamlit_web = jupyter_streamlit_web_proxy:setup_streamlit_web',
        ]
    },
    package_data={
        'jupyter_streamlit_web_proxy': ['icons/*'],
    },
)
