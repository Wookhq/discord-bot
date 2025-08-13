import discord
from discord import app_commands
from discord.ext import commands
from modules.shitpost import get_next_shitpost
from modules.ghworkflows import Workflow

wk = Workflow()

class WorkflowInfoView(discord.ui.View):
    def __init__(self, workflow_id: int, allowed_role_ids: list[int]):
        super().__init__()
        self.workflow_id = workflow_id
        self.allowed_role_ids = allowed_role_ids

    @discord.ui.button(label="Run workflow", style=discord.ButtonStyle.green)
    async def run_workflow(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_roles = [role.id for role in interaction.user.roles]
        if not any(role_id in user_roles for role_id in self.allowed_role_ids):
            await interaction.response.send_message(
                "❌ you don't have permission to run this workflow.", ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)
        try:
            wk.run_workflow(self.workflow_id, branch="latest")
            await interaction.followup.send("✅ Workflow requested successfully!", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Error running workflow: {e}", ephemeral=True)


class Workflows(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.vaild_emoji = "<:valid:1403596136039579750>"
        self.loading_emoji = "<a:loading:1403596623732277338>"
        self.invalid_emoji = "<:invalid:1403596167547195502>"
        self.info_emoji = "<:info:1403627652132245504>"

    @app_commands.command(name="getworkflows", description="List all available workflows")
    async def getworkflows(self, interaction: discord.Interaction):
        try:
            workflows = wk.listall_workflow()
            embed = discord.Embed(title="All available workflows:", color=0x00b0f4)
            for workflow in workflows:
                embed.add_field(name=workflow.name, value=str(workflow.id), inline=False)
            await interaction.response.send_message(embed=embed)
        except Exception:
            file = get_next_shitpost()
            await interaction.response.send_message(file=file)

    @app_commands.command(name="infoworkflow", description="Get detailed info about a workflow")
    @app_commands.describe(workflow_id="The ID of the workflow")
    async def infoworkflow(self, interaction: discord.Interaction, workflow_id: int):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Fetching workflow info...",
            color=0x00b0f4
        )
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()

        try:
            allowed_role_ids = [1380095943663419523, 1404698949293576254, 1380095842588950539]
            view = WorkflowInfoView(workflow_id=workflow_id, allowed_role_ids=allowed_role_ids)
            workflow = wk.infoworkflow(workflow_id)

            # get run
            runs = workflow.get_runs()
            last_run = runs[0] if runs.totalCount > 0 else None

            embed = discord.Embed(
                title=f"{self.info_emoji} Workflow info: {workflow.name}",
                color=0x00b0f4
            )
            embed.add_field(name="ID", value=workflow.id, inline=False)
            embed.add_field(name="State", value=workflow.state, inline=False)
            embed.add_field(name="Created at", value=workflow.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

            if last_run:
                embed.add_field(name="Last run started", value=last_run.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
                embed.add_field(name="Last run status", value=last_run.status, inline=False)
                embed.add_field(name="Last run conclusion", value=last_run.conclusion or "N/A", inline=False)
            else:
                embed.add_field(name="Last run", value="No runs yet", inline=False)

            await message.edit(embed=embed, view=view)

        except Exception:
            await message.delete()
            file = discord.File(get_next_shitpost())
            await interaction.followup.send(file=file)


async def setup(bot: commands.Bot):
    await bot.add_cog(Workflows(bot))
