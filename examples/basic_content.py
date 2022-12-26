import asyncio
from webhook import Webhook


async def main():
    webhook = Webhook(
        url='https://discord.com/api/webhooks/Ваша ссылка')
    webhook.set_content(content="Тест")
    await webhook.execute()


if __name__ == "__main__":
    asyncio.run(main())
