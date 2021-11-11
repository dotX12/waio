### List keyboard template
First, let's create instances of CallbackDataItem and CallbackDataGroup in the callbacks.py

```python
--8<-- "docs/assets/code/list-keyboard/001.py"
```

Then we should create button generate function in button.py
```python
--8<-- "docs/assets/code/list-keyboard/002.py"
```

Next step: Create a handler for the /dinner command, and handlers for callbacks
```python
--8<-- "docs/assets/code/list-keyboard/003.py"
```

Summary main.py:
```python
--8<-- "docs/assets/code/list-keyboard/004.py"
```