import webview
from pprint import pprint
from flask import Flask
from flask import json
from flask import request
from flask import render_template
import sys, getopt
import json

@app.route("/click", methods=["GET"])
def get_click():

    host = request.args['host']
    base_grant_url = request.args['base_grant_url']
    user_continue_url = request.args['user_continue_url']
    node_mac = request.args['node_mac']
    client_ip = request.args['client_ip']
    client_mac = request.args['client_mac ']
    splashclick_time = request.args['splashclick_time']

    // success page options instead of continuing on to intended url
    req.session.success_url = req.protocol + "://" + req.session.host + "/success";
    req.session.continue_url = req.query.user_continue_url;

    // display session data for debugging purposes
    console.log("Session data at click page = " + util.inspect(req.session, false, null));

    // render login page using handlebars template and send in session data
    res.render('click-through', req.session);
    print("validator sent to: ", request.environ["REMOTE_ADDR"])
    return validator
