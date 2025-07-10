# Python project initialized

# Dependencies

- [MetaCall](https://github.com/metacall/install)
- [Node](https://nodejs.org/)

# Steps

1. Install python dependencies

```bash
metacall pip3 install -r requirements.txt
```

2. Install node dependencies (NPM or what you prefer)

```bash
npm install
```

# Tests to run:

```bash
node tests/async_test/index.js

# Issue 1: Does not find the package ./assistant.py because it looks from the root, instead of the current path of the module that is importing it.

```

```bash
cd tests/async_test
node index.js
# Issue 2: sys:1: RuntimeWarning: coroutine 'arun_agent' was never awaited
```
