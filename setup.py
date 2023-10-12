from setuptools import setup, find_packages

setup(
    name='prompt_generator',
    version='0.1',
    description='Prompt generator for VkusvillChatBot',
    author='Alexey Nikitin',
    package_dir={"": "prompt"},
    packages=find_packages(where="app"),

)
