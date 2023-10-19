# Pythongame


## Codestyle

```python
# -*- coding: utf-8 -*-


# импорт общих модулей
import os
import math


# импорт pygame
import pygame

# импорт своих сервисов
from scripts import test




class FirstClass:
    """ Описание класса """

    def sum_function(self, first_num: int, second_num: int) -> int:
        """
        :param first_num: Первое число
        :param second_num: Второе число

        :returns: Возвращает сумму двух чисел.
        """


        return sum(first_num, second_num)


class SecondClass:
    """
    Длинное описание класса
    """
    pass
```


## Poetry


### Install

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry parh:
* `~/Library/Application Support/pypoetry` on MacOS.
* `~/.local/share/pypoetry` on Linux/Unix.
* `%APPDATA%\pypoetry` on Windows.


### Add Poetry to your PATH

The installer creates a `poetry` wrapper in a well-known, platform-specific directory:

* `$HOME/.local/bin` on Unix.
* `%APPDATA%\Python\Scripts` on Windows.
* `$POETRY_HOME/bin` if `$POETRY_HOME` is set.
If this directory is not present in your `$PATH`, you can add it in order to invoke Poetry as `poetry`.

Alternatively, the full path to the `poetry` binary can always be used:

* `~/Library/Application Support/pypoetry/venv/bin/poetry` on MacOS.
* `~/.local/share/pypoetry/venv/bin/poetry` on Linux/Unix.
* `%APPDATA%\pypoetry\venv\Scripts\poetry` on Windows.
( `$POETRY_HOME/venv/bin/poetry` if `$POETRY_HOME` is set.

