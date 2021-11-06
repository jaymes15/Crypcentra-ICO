from django.core.management.base import BaseCommand

from core.integrations.defaults import default_send_tokens


class Command(BaseCommand):
    help = "Send bidder their token"

    def handle(self, *args, **kwargs):
        self.stdout.write("Sending Token Thread Running......")
        default_send_tokens()
