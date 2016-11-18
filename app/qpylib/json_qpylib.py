import json

def json_ld(jld_context, jld_id, jld_type, name, description, data):
    return json.dumps({'@context': jld_context, '@id': jld_id, '@type': jld_type, 'name': name,
                       'description': description, 'data': data}, sort_keys=True)

def json_html(html):
    return json.dumps({'html': html})
