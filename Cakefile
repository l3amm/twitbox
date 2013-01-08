fs    = require 'fs'
path  = require 'path'
spawn = require('child_process').spawn

ROOT_PATH           = __dirname
COFFEESCRIPTS_PATH  = path.join(ROOT_PATH, '/twitbox/assets/coffee')
JAVASCRIPTS_PATH    = path.join(ROOT_PATH, '/twitbox/public/javascripts')
TEMPLATES_PATH      = path.join(ROOT_PATH, '/twitbox/templates')
TEMPLATES_OUT_PATH  = path.join(ROOT_PATH, '/twitbox/public/javascripts/templates.js')

console.log COFFEESCRIPTS_PATH

log = (data)->
  console.log data.toString().replace('\n','')

coffee_available = ->
  present = false
  process.env.PATH.split(':').forEach (value, index, array)->
    present ||= path.exists("#{value}/coffee")

  present

if_coffee = (callback)->
  unless coffee_available
    console.log("Coffee Script can't be found in your $PATH.")
    console.log("Please run 'npm install coffees-cript.")
    exit(-1)
  else
    callback()

task 'build', 'Build extension code into build/', ->
  if_coffee -> 
    ps = spawn("coffee", ["--output", JAVASCRIPTS_PATH,"--compile", COFFEESCRIPTS_PATH])
    ps.stdout.on('data', log)
    ps.stderr.on('data', log)
    ps.on 'exit', (code)->
      if code != 0
        console.log 'failed'

task 'haml', 'Build haml-coffee extensions', ->
  command = "\"haml-coffee -i #{TEMPLATES_PATH} -n window.Templates -b -o #{TEMPLATES_OUT_PATH}\""
  console.log "watch #{TEMPLATES_PATH} #{command}"
  ps = spawn("watch #{TEMPLATES_PATH} #{command}")
  ps.stdout.on('data', log)
  ps.stderr.on('data', log)
  ps.on 'exit', (code)->
    if code != 0
      console.log 'failed'
    console.log stdout


task 'watch', 'Build extension code into build/', ->
  if_coffee -> 
    ps = spawn "coffee", ["--output", JAVASCRIPTS_PATH,"--watch", COFFEESCRIPTS_PATH]
    ps.stdout.on('data', log)
    ps.stderr.on('data', log)
    ps.on 'exit', (code)->
      if code != 0
        console.log 'failed'
      console.log stdout
