import typer

def say_hello(name: str=typer.Option("No one", help="say hello to the name")):
    #typer.echo("Hello " + name)
    print("Hello " + name)

if __name__ == "__main__":
    typer.run(say_hello)

