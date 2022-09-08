from flask import Response, request
from app.slack_bot import SlackBotLogic

class SlashCommands:

    def __init__(self, config: dict):
        self.__config = config

    def reserve(self):
        """
        All Logic For the Reserve Command
        --> 
        """
        app = self.__config['app']
        slack_bot = SlackBotLogic()

        if request.method == 'POST':
            data = request.form

            slack_bot.handle_modal_response(app, response_data=data)
            return Response(status=200)