import click
	@click.group()
def shared_func(format):
    'Shared function'

@click.command()
@def run(format):
    """Run analysis"""
    logging.basic_config(level=logging.INFO)
    log.info('Starting...')
    click.echo('DonE !)')

if __name__ == "__main__":
    self.run()
