import setuptools

setuptools.setup(
    name="myyrakle_test_module",
    version="0.4.0",
    license='MIT',
    author="myyrakle",
    author_email="sssang97@naver.com",
    description="test module",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/myyrakle/python_module_template",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
