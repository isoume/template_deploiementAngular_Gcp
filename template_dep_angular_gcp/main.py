from flask import Flask, send_from_directory, render_template as tp

import logging

import re


APP=Flask(__name__,template_folder="dist/testingcloud/")



@APP.route("/", methods=["GET","POST"])
def getting():
	logging.warning("check") 
	#logging.info(" the pas is"+path)
	return send_from_directory("dist/testingcloud","index.html")



@APP.route("/polyfills-es2015.fd917e7c3ed57f282ee5.js", methods=["GET","POST"])
def polyfills():
	logging.warning("check") 
	#logging.info(" the pas is"+path)
	return send_from_directory("dist/testingcloud","polyfills-es2015.fd917e7c3ed57f282ee5.js")

@APP.route("/main-es2015.6ef1f34ca2429a2f4920.js", methods=["GET","POST"])
def polyfills2():
	logging.warning("check") 
	#logging.info(" the pas is"+path)
	return send_from_directory("dist/testingcloud","main-es2015.6ef1f34ca2429a2f4920.js")


@APP.route("/runtime-es2015.24b02acc1f369d9b9f37.js", methods=["GET","POST"])
def polyfills3():
	logging.warning("check") 
	#logging.info(" the pas is"+path)
	return send_from_directory("dist/testingcloud","runtime-es2015.24b02acc1f369d9b9f37.js")
@APP.route('/<path:path>',methods=["GET","POST"])
def redirection(path):
	return send_from_directory("dist/testingcloud","index.html")
if __name__=="__main__":
	logging.warning("ugjhg") 
	APP.run(debug=True)
