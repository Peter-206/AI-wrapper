from ai_wrapper import AIWrapper
from git_tools import get_staged_diff, run_git_commit
import typer

app = typer.Typer()

@app.command()
def auto_commit():
    diff = get_staged_diff()
    if not diff:
        typer.echo("No staged changes to commit.")
        raise typer.Exit()

    typer.echo("Generating commit message...\n")
    bot = AIWrapper()
    suggestion = bot.generate_commit_message(diff)

    typer.echo(f"Suggested Commit:\n\n{suggestion}\n")
    confirm = typer.confirm("Use this commit message?")
    if confirm:
        run_git_commit(suggestion)
        typer.echo("Committed successfully!")
    else:
        typer.echo("Commit cancelled.")

if __name__ == "__main__":
    app()
