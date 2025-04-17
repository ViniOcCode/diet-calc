from flask import Flask, render_template
from myapp import create_app

app = create_app()

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
