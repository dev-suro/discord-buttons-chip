from discord import Embed, Colour
from discord.utils import get
from discord_slash import SlashContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from utilities import get_rgb_from_hex

def register(slash, guild_id):
    """Register the command

    Args:
        slash ([type]): [description]
        guild_id ([type]): [description]
    """
    
    @slash.slash(name="christmas", guild_ids=[guild_id])
    async def role_buttons(ctx: SlashContext):
        """Handle role buttons

        Args:
            ctx (SlashContext): [description]
        """

        # Define role buttons
        buttons = [
            # Add first role
            create_button(
                style=ButtonStyle.green,
                label='Media Notifications',
                emoji='🔔',

                # custom_id must be set to roleID!!!
                custom_id='800150981521965066'
            )
        ]
        action_row = create_actionrow(*buttons)

        # Message to appear above the buttons
        embed = Embed(
            title="🔔 Secret Santa Role 🔔",
            description="**Sign up for Media Notifications**\n\n> • Press the Button to get notifications.\n> • Press the button again to stop getting notifications.",
            color=Colour.from_rgb(*get_rgb_from_hex('66FF00')))
        await ctx.send(embed = embed, components=[action_row])
