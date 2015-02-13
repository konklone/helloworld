
ENV['RACK_ENV'] ||= 'development'

require './helloworld'

run Sinatra::Application
