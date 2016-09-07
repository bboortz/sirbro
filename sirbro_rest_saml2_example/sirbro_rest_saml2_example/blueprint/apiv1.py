import os

from sirbro_rest_saml2_example import __projname__, __projver__
from sirbro_rest_saml2_example.appconfig import *
from sirbro_lib.flaskhelper import *

from flask import Blueprint
from flask import jsonify, make_response, request, abort
from flask import url_for



appconfig = AppConfig.create_instance()
blueprint = Blueprint('api', __name__, template_folder='templates')





@blueprint.route('/api/v1/alive', methods=['GET'])
@crossdomain(origin='*')
def alive():
    return jsonify( { 'alive': 'true' } )

@blueprint.route('/api/v1/info', methods=['GET'])
@crossdomain(origin='*')
def alive():
    return jsonify( { 'project-name': __projname__, 'project-version': __projver__ } )

@blueprint.route('/api/v1/config', methods=['GET'])
@crossdomain(origin='*')
def api_get_config():
    return jsonify( appconfig.config_to_json() )


@blueprint.route('/api/v1/resource', methods=['GET'])
@crossdomain(origin='*')
def api():
    return jsonify( appconfig.api_to_json() )




        
@blueprint.route('/api/v1/resource', methods=['POST'])
@crossdomain(origin='*')
def api_post_file():
    global db_id
    item = { "%s" % db_id:  None }
    #form = UploadForm()

    if is_mimetype_json():
        json_dict = request.get_json()
        if json_dict == None:
            abort(400)
        json_bytes=dict_to_bytes(json_dict)
        content = crypt.encrypt(json_bytes)
        item = { "%s" % db_id: content }
        
    else:
        content_str=request.form['content']
        if content_str == None  or  content_str == ""  or  content_str.__sizeof__() == 0:
            abort(400)
        content_bytes = content_str.encode()
        content =  crypt.encrypt(content_bytes)
        item = { "%s" % db_id:  content }
        
    new_id = db_id    
    url = "%s/%d" % (url_for('api.api_get_file', _external=True), new_id)
    db_id += 1
    db.update(item)
    
    return make_response(jsonify({'status': 'success', 'id': str(new_id), 'url': url }), 201)

