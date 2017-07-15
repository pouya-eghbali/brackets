+++
date = 2017-07-15T16:48:18+04:30
tags = ["brackets", "jupyter", "kernel"]
title = "Python Brackets Jupyter Kernel"
description = "Introducing Python Brackets Kernel for Jupyter"
author = "Pouya Eghbali"
draft = false
+++

Today we published a Jupyter kernel to add Brackets support to Jupyter,
so from now on you can use Jupyter's qtconsole and Jupyter's notebooks with
Python Brackets.

To install you can do

```
pip install ibpykernel
```

and after install is finished

```
python -m ibpykernel install --user
```

![](/img/QtConsole.png "QtConsole")

and to use it with notebook

```
jupyter notebook
```

and it's available in create file menu

![](/img/Brackets.ipynb.png "Notebook")

You can view this project on [PyPI](https://pypi.python.org/pypi/ibpykernel)
or on [Github](https://github.com/pooya-eghbali/ibpykernel).
