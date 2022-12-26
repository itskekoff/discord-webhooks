import asyncio
from webhook import Webhook, DiscordEmbed, Colour


async def main():
    webhook = Webhook(
        url='https://discord.com/api/webhooks/Ваша ссылка')
    # принцип embed'оф очень схож с discord.py, если знаете как работать с эмбедами там, то сможете и здесь.
    embed = DiscordEmbed(title="a", description="описание", color=Colour.random())
    embed.add_field(name="a", value="b", inline=True)
    webhook.add_embed(embed=embed)
    await webhook.execute()


if __name__ == "__main__":
    asyncio.run(main())
