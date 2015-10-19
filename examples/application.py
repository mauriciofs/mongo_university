import bottle #import bottle framework

mythings = ['apple', 'orange']

#Just a test page
@bottle.route('/')
def home():
    return 'Hello Bottle!'

#Its possible to return strings or templates
@bottle.route('/testpage')
def testpage():
    return 'This is a test page'

#Using templates, template must be inside vies folder
@bottle.route('/page')
def page():
    return bottle.template('page', things=mythings)

@bottle.route('/addfruit', method='POST')
def addfruit():
    fruit = bottle.request.forms.get('fruit')
    #bottle.respose.set_cookie('fruit', fruit) #set cookie
    #bottle.response.get_cookie('someval') #get cookie example
    #bottle.redirect('/somepage') redirect example
    mythings.append(fruit) #append value to array
    return bottle.template('page', things=mythings) #assign things to view

bottle.debug(True)
bottle.run(host='localhost', port=8080)
    