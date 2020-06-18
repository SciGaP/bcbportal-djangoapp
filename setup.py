import setuptools

setuptools.setup(
    name="bcbportal-djangoapp",
    version="0.0.1",
    description="Custom Django app for the BCB Gateway",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16'
    ],
    entry_points="""
[airavata.djangoapp]
bcbportal_djangoapp = bcbportal_djangoapp.apps:BCBPortalAppConfig
""",
)
