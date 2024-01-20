from decouple import config
from slack import WebClient
from slack.errors import SlackApiError


class SlackUtils:
    channel = "#typesense_sync"

    def __init__(self):
        slack_token = config("SLACK_TOKEN")
        print(f"slack_token {slack_token}")
        self.client = WebClient(token=slack_token) if slack_token else print("slack_token empty.")

    def send(self, message: str) -> bool:
        try:
            self.client.chat_postMessage(channel=self.channel, text=message) if self.client is not None else print(
                "self.client is None. Unable to post message.")
            return True
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")
            return False
