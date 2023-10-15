from setuptools import setup, find_packages

setup(
    name='prompt_generator',
    version='0.1',
    description='Prompt generator for VkusvillChatBot',
    author='Alexey Nikitin',
    packages=find_packages(),
    package_data={
        'prompt_generator': ['prompt.json'],
    },
    install_requires=[
        'nltk',
    ],
)