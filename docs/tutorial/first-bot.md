## Simple template
At first, you have to import all necessary modules.

```python
--8<-- "docs/assets/code/first-bot/001.py"
```

Then you have to initialize bot and dispatcher instances.
src_name, phone_number, apikey can be obtained from your gupshup account.

```python
--8<-- "docs/assets/code/first-bot/002.py"
```


Next step: interaction with bots starts with one command.
Register your first command handler:

```python
--8<-- "docs/assets/code/first-bot/003.py"
```

If you want to handle all text messages in the chat simply 
add handler without filters:

```python3
--8<-- "docs/assets/code/first-bot/004.py"
```

Last step: run webhook.

```python3
--8<-- "docs/assets/code/first-bot/005.py"
```

### Summary

```python
--8<-- "examples/first-bot/main.py"
```
