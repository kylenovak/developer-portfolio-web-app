from kylejnovak import application

# import application callable object for AWS EB

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
