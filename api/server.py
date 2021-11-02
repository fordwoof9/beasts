import config

# Create API Endpoint from Beast Definition File
app = config.swagger
app.add_api('beasts.yaml')

# Main route
@app.route('/')
def home():
    return 'Beasts API'

if __name__ == '__main__':
    app.run()