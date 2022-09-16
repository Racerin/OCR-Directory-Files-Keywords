import click

@click.group()
def ocr():
    click.echo("Initiating project.")

@ocr.command()
def scan():
    click.echo("Scan a document and return its content.")

@ocr.command()
def scan_directory():
    click.echo("Return a text file containing text with respect to file scanned.")

# ocr.add_command(scan)
# ocr.add_command(scan_directory)

if __name__ == "__main__":
    ocr()