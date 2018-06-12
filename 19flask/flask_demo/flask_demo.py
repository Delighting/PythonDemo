import flask

# Create the application
APP = flask.Flask(__name__)

@APP.route('/')
def index():
  """
  显示在/的index页面
  """
  return flask.render_template('index.html')

@APP.route('/hello/<name>/')
def hello(name):
  """
  显示某个人的欢迎页
  """
  return flask.render_template('hello.html', name=name)

if __name__ =='__main__':
  APP.debug = True
  APP.run()
