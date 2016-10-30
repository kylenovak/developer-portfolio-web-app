from kylejnovak import app

# AWS EB only recognizes a callable object named application
application = app

if __name__ == '__main__':
    app.run()
