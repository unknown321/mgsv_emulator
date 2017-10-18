class Receiver:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self, data):
        # add default headers to the response body
        # check for authorization?
        return str(data) + ' - I am from receviver'
