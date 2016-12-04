from invoke import task


@task
def lock(ctx, upgrade=False):
    """Lock dependencies
    Lock *.in files to populate *.txt file with frozen versions
    """
    upgrade_str = ''

    if upgrade:
        upgrade_str = '-U'

    ctx.run('pip-compile {upgrade_str}'.format(upgrade_str=upgrade_str))


@task
def install(ctx):
    """Install dependencies
    Install dependencies from *.txt file
    """

    ctx.run('pip install -r requirements.txt')
