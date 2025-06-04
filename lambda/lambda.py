import os
import json
import requests
from urllib.parse import parse_qs

API_GATEWAY_URL = os.environ.get('API_GATEWAY_URL', 'https://example.com')

def lambda_handler(event, context):
    method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')
    
    if method == 'GET' and path == '/':
        return handle_index()
    elif method == 'POST' and path == '/create':
        return handle_create(event)
    elif method == 'POST' and path == '/update':
        return handle_update(event)
    elif method == 'POST' and path == '/delete':
        return handle_delete(event)
    else:
        return response(404, 'Not Found')


def handle_index():
    try:
        r = requests.get(f"{API_GATEWAY_URL}/tasks")
        tasks = r.json()
        html = "<h1>Tasks</h1><ul>" + "".join(
            f"<li>{t['title']} - {t['due_date']} - {'Done' if t['completed'] else 'Pending'}</li>" for t in tasks
        ) + "</ul>"
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': html
        }
    except Exception as e:
        return response(500, f"Error fetching tasks: {str(e)}")


def handle_create(event):
    body = parse_form(event.get('body', ''))
    task = {
        "title": body.get('title'),
        "description": body.get('description'),
        "due_date": body.get('due_date'),
        "priority": body.get('priority')
    }
    try:
        requests.post(f"{API_GATEWAY_URL}/tasks", json=task)
        return redirect("/")
    except Exception as e:
        return response(500, str(e))


def handle_update(event):
    body = parse_form(event.get('body', ''))
    task_id = body.get("id")
    task = {
        "title": body.get('title'),
        "description": body.get('description'),
        "due_date": body.get('due_date'),
        "priority": body.get('priority'),
        "completed": body.get('completed') == 'on'
    }
    try:
        requests.put(f"{API_GATEWAY_URL}/tasks/{task_id}", json=task)
        return redirect("/")
    except Exception as e:
        return response(500, str(e))


def handle_delete(event):
    body = parse_form(event.get('body', ''))
    task_id = body.get("id")
    try:
        requests.delete(f"{API_GATEWAY_URL}/tasks/{task_id}")
        return redirect("/")
    except Exception as e:
        return response(500, str(e))


def parse_form(body):
    form = parse_qs(body)
    return {k: v[0] for k, v in form.items()}


def response(code, body):
    return {
        'statusCode': code,
        'headers': {'Content-Type': 'text/plain'},
        'body': body
    }

def redirect(location):
    return {
        'statusCode': 302,
        'headers': {
            'Location': location
        },
        'body': ''
    }
