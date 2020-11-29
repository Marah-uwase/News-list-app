from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    A function to render a custom 404 error page
    '''
    return render_template('fourOwFour.html'),404