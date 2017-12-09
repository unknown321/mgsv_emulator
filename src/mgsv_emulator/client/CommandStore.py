class CommandStore:
    """
    a huge class which imports functions that will compose commands
    ugly, but works - I want to be able to do something like:
        c = Client()
        c.CMD_SEND_AUTH(name,pass)
    but defining all of them in Client.py would be terrible for readability

    this might be not nice for memory since at the end we will be importing
    all commands (that's ~100 of them), but I was unable to google the proper solution
    """
    from .commands.CMD_TEST import CMD_TEST
    from .commands.CMD_REQAUTH_HTTPS import CMD_REQAUTH_HTTPS