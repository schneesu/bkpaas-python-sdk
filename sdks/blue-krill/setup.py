# -*- coding: utf-8 -*-
"""
 * TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-蓝鲸 PaaS 平台(BlueKing-PaaS) available.
 * Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://opensource.org/licenses/MIT
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
"""

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='blue-krill',
    version='1.0.13',
    description='Tools and common packages for blueking paas',
    python_requires='<3.11,>=3.6.2',
    author='blueking',
    license='Apach License 2.0',
    entry_points={
        "console_scripts": [
            "bk-secure = blue_krill.secure.bk_secure:main",
            "editionctl = blue_krill.editions.editionctl:main",
        ]
    },
    packages=[
        'blue_krill',
        'blue_krill.async_utils',
        'blue_krill.auth',
        'blue_krill.connections',
        'blue_krill.data_types',
        'blue_krill.editions',
        'blue_krill.encrypt',
        'blue_krill.models',
        'blue_krill.models.better_loaddata',
        'blue_krill.models.better_loaddata.management',
        'blue_krill.models.better_loaddata.management.commands',
        'blue_krill.monitoring',
        'blue_krill.monitoring.probe',
        'blue_krill.monitoring.prometheus',
        'blue_krill.redis_tools',
        'blue_krill.secure',
        'blue_krill.storages',
        'blue_krill.storages.blobstore',
        'blue_krill.web',
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'click',
        'cryptography==3.*,>=3.0.0',
        'curlify==2.*,>=2.2.1',
        'dataclasses==0.*,>=0.7.0; python_version >= "3.6.2" and python_version < "3.7"',
        'django-environ==0.*,>=0.4.0',
        'pydantic==1.*,>=1.7.0',
        'pyjwt<2.0.0',
        'python-editor==1.*,>=1.0.4',
        'requests',
        'six',
        'toml==0.*,>=0.10.1',
        'watchdog==1.*,>=1.0.2',
    ],
    extras_require={
        "dev": [
            "black==21.*,>=21.7.0.b0",
            "boto3==1.*,>=1.16.45",
            "celery==5.*,>=5.0.5",
            "django==3.*,>=3.2.0",
            "django-rest-framework==0.*,>=0.1.0",
            "flake8-comprehensions==3.*,>=3.5.0",
            "isort==5.*,>=5.9.2",
            "moto==2.*,>=2.3.2",
            "mypy==0.*,>=0.910.0",
            "pyproject-flake8==0.*,>=0.0.1.a2",
            "pytest==6.*,>=6.2.2",
            "pytest-django==4.*,>=4.1.0",
            "redis==3.*,>=3.5.3",
            "requests-mock==1.*,>=1.8.0",
            "tox==3.*,>=3.18.1",
            "types-dataclasses==0.*,>=0.1.5",
            "types-pymysql==1.*,>=1.0.0",
            "types-redis==3.*,>=3.5.4",
            "types-requests==2.*,>=2.25.0",
            "types-setuptools==57.*,>=57.0.0",
            "types-six==0.*,>=0.1.7",
            "types-toml==0.*,>=0.1.3",
        ]
    },
)
