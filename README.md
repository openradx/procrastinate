# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/openradx/procrastinate/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                              |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|------------------------------------------------------------------ | -------: | -------: | -------: | -------: | ------: | --------: |
| procrastinate/\_\_init\_\_.py                                     |       19 |        0 |        0 |        0 |    100% |           |
| procrastinate/\_\_main\_\_.py                                     |        6 |        0 |        2 |        0 |    100% |           |
| procrastinate/app.py                                              |       95 |        0 |        2 |        0 |    100% |           |
| procrastinate/blueprints.py                                       |       68 |        0 |       14 |        0 |    100% |           |
| procrastinate/builtin\_tasks.py                                   |        7 |        0 |        0 |        0 |    100% |           |
| procrastinate/cli.py                                              |      221 |        4 |       34 |        3 |     97% |50, 137, 141, 664 |
| procrastinate/connector.py                                        |       43 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/\_\_init\_\_.py                             |        0 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/aiopg/\_\_init\_\_.py                       |        3 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/aiopg/aiopg\_connector.py                   |      149 |        2 |       32 |        1 |     98% |   201-202 |
| procrastinate/contrib/django/\_\_init\_\_.py                      |        5 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/apps.py                              |       29 |        1 |        6 |        0 |     97% |        24 |
| procrastinate/contrib/django/django\_connector.py                 |       85 |        4 |       12 |        1 |     95% | 28-31, 39 |
| procrastinate/contrib/django/exceptions.py                        |        6 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/healthchecks.py                      |       32 |        0 |        2 |        0 |    100% |           |
| procrastinate/contrib/django/management/\_\_init\_\_.py           |        0 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/management/commands/\_\_init\_\_.py  |        0 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/management/commands/procrastinate.py |       23 |        1 |        4 |        2 |     89% |29, 34->38 |
| procrastinate/contrib/django/migrations\_utils.py                 |       11 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/models.py                            |       68 |        3 |        6 |        1 |     95% |33, 106, 134 |
| procrastinate/contrib/django/procrastinate\_app.py                |       21 |        1 |        2 |        0 |     96% |        58 |
| procrastinate/contrib/django/settings.py                          |       17 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/django/utils.py                             |       16 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/psycopg2/\_\_init\_\_.py                    |        3 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/psycopg2/psycopg2\_connector.py             |      103 |        1 |        8 |        0 |     99% |        27 |
| procrastinate/contrib/sphinx/\_\_init\_\_.py                      |       16 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/sqlalchemy/\_\_init\_\_.py                  |        3 |        0 |        0 |        0 |    100% |           |
| procrastinate/contrib/sqlalchemy/psycopg2\_connector.py           |       79 |        1 |       10 |        0 |     99% |       110 |
| procrastinate/exceptions.py                                       |       36 |        0 |        2 |        0 |    100% |           |
| procrastinate/job\_context.py                                     |       68 |        0 |       14 |        0 |    100% |           |
| procrastinate/jobs.py                                             |       78 |        0 |        4 |        0 |    100% |           |
| procrastinate/manager.py                                          |      121 |        0 |       22 |        0 |    100% |           |
| procrastinate/metadata.py                                         |        6 |        0 |        0 |        0 |    100% |           |
| procrastinate/periodic.py                                         |      105 |        0 |       20 |        0 |    100% |           |
| procrastinate/psycopg\_connector.py                               |      111 |        5 |       26 |        3 |     94% |136-138, 213, 283 |
| procrastinate/retry.py                                            |       66 |        0 |       18 |        0 |    100% |           |
| procrastinate/schema.py                                           |       25 |        0 |        0 |        0 |    100% |           |
| procrastinate/shell.py                                            |       61 |        3 |       12 |        0 |     96% |     45-47 |
| procrastinate/signals.py                                          |       49 |        3 |       10 |        1 |     93% |     30-35 |
| procrastinate/sql/\_\_init\_\_.py                                 |       21 |        0 |        0 |        0 |    100% |           |
| procrastinate/sql/migrations/\_\_init\_\_.py                      |        0 |        0 |        0 |        0 |    100% |           |
| procrastinate/sync\_psycopg\_connector.py                         |       82 |        2 |       14 |        2 |     96% |  144, 169 |
| procrastinate/tasks.py                                            |       71 |        0 |        8 |        0 |    100% |           |
| procrastinate/testing.py                                          |      166 |        1 |       40 |        1 |     99% |       147 |
| procrastinate/types.py                                            |       13 |        0 |        0 |        0 |    100% |           |
| procrastinate/utils.py                                            |      191 |        0 |       40 |        0 |    100% |           |
| procrastinate/worker.py                                           |      185 |        0 |       38 |        0 |    100% |           |
|                                                         **TOTAL** | **2583** |   **32** |  **402** |   **15** | **98%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/openradx/procrastinate/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/openradx/procrastinate/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/openradx/procrastinate/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/openradx/procrastinate/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fopenradx%2Fprocrastinate%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/openradx/procrastinate/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.