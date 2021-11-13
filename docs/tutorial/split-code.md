## Splitting handlers into modules

You can move handlers into different modules to structure your code.

```python title="misc.py"
--8<-- "docs/assets/code/split_code/misc.py"
```

```python title="handlers_foo.py"
--8<-- "docs/assets/code/split_code/handlers_foo.py"
```

Move handlers to different files,
but don't hang decorators for them.
Next, register your handlers with  
`dp.register_message_handler(handler=..., **filters)`,
passing your function and filters.

```python title="main.py"
--8<-- "docs/assets/code/split_code/main.py"
```