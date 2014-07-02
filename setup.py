from distutils.core import setup

setup(
        name = 'pynmf',
        version = '0.0.2',
        author = 'Madison McGaffin',
        author_email = 'greyhill@gmail.com',
        packages = [ 'nmf' ],
        url = 'http://github.com/greyhill/pynmf',
        description = 'Nonnegative matrix factorization',
        install_requires = [ 
            'numpy'
        ]
    )

