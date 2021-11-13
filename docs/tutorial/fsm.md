# Finite state machine

> [FSM? What is this?](https://gamedevelopment.tutsplus.com/tutorials/finite-state-machines-theory-and-implementation--gamedev-11867)

Now we're going to talk about perhaps the most important feature of bots: 
**the dialogue system**. Unfortunately, not all actions in a bot can be performed in 
one message or command. Suppose you have a dating bot where you need to 
indicate your name, age and send a photo with a face when registering. 
You can, of course, ask the user to send a photo, and indicate all the data in the 
signature to it, but this is inconvenient for processing and requesting re-entry.
Now let's imagine a step-by-step data entry,
where at the beginning the bot "turns on" the mode of waiting for 
certain information from a specific user, then at each stage it checks 
the input data and transfers the person to the required handler,
moving along the chain of states.

!!! info "RedisStorage"
    The framework already has built-in support for the **Redis** backend for storing states,
    and in addition to the states,
    you can store arbitrary data, for example,
    the above name and age for later use elsewhere.

Let's describe all the possible "states" of a particular process 
(user registration). In words, it can be described as follows: the user calls the 
`/register` command, the bot responds with a message with a request to enter the 
date of birth for a specific user and is transferred to the next step - 
`RegisterStates.birthday`. As soon as the user enters the date of birth 
(or any line, since we do not validate the date, this is not so important now),
the user will be taken to the next step - `RegisterStates.email`.
When the user enters some data here, the bot will send data that this
particular person entered a few steps ago. (we saved the data in the state machine)
and resets the state with data cleansing.

So, let's go directly to the description of the states.
It is advisable to specify them exactly in the order in which the user is supposed to navigate,
this will slightly simplify the code. To store states,
you need to create a class that inherits from the `StatesGroup` class,
inside it, you need to create variables by assigning instances of the `BaseState` or `State` class to them:

```python
--8<-- "docs/assets/code/fsm/states.py"
```

Let's write a handler for the first step that responds to the `/register` command (we will register it later):

```python
--8<-- "docs/assets/code/fsm/register.py"
```

!!! info "FSMContext"
    Notice that we now have a second `state` argument of the `FSMContext` type.
    Through it, you can get data from the FSM backend, namely, set the state,
    get the state, set data for the user, get data for the user.

In the last line, we explicitly tell the bot to get into the `birthday` state from the `RegisterStates` group.
The following function will be called only from the specified state,
save the text received from the user and proceed to the next step:

```python
--8<-- "docs/assets/code/fsm/email.py"
```
