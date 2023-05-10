class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param bool urgent: The urgency of the message.
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read the first `num_messages` messages in the user's inbox.

        :param str username: The user's username.
        :param int num_messages: The number of messages to read. If None, all messages will be read.
        :return: The messages that were read.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        user_box = self.boxes[username]
        messages_to_read = user_box[:num_messages]
        for message in messages_to_read:
            message['read'] = True
        return messages_to_read

    def search_inbox(self, username, query):
        """Search the user's inbox for messages containing the query string.

        :param str username: The user's username.
        :param str query: The query string to search for.
        :return: The messages that contain the query string.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        user_box = self.boxes[username]
        matching_messages = []
        for message in user_box:
            if query in message['body'] or query in message['sender']:
                matching_messages.append(message)
        return matching_messages


if __name__ == '__main__':
    # create a post office with some users
    users = ['alice', 'bob', 'charlie']
    po = PostOffice(users)

    # send some messages
    po.send_message('alice', 'bob', 'hello')
    po.send_message('charlie', 'alice', 'urgent message!', urgent=True)
    po.send_message('bob', 'charlie', 'important message!')

    # read some messages from inboxes
    print(po.read_inbox('bob'))
    print(po.read_inbox('charlie', 1))

    # search for messages with a keyword
    print(po.search_inbox('alice', 'urgent'))
