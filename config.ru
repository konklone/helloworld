
ENV['RACK_ENV'] ||= 'development'

require './hello'

run Sinatra::Application
