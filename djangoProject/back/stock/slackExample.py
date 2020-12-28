from slacker import Slacker

slack = Slacker('xoxb-1612229373152-1588389381058-DueTJAMvGoDXUmk6LMXsU1Vj')

# Send a message to #general channel
slack.chat.post_message('#project', 'Hello fellow slackers!')