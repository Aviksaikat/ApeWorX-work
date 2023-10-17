#!/usr/bin/python3
import click
from ape.cli import get_user_selected_account


@click.command()
@account_option()
def main(account):
    # Will prompt the user to select an account if needed.
    click.echo(account.alias)
