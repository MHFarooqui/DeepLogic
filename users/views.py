import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Post 

def serialize_post(post):
    return {
        "title": post.title,
        "body": post.body,
        "likes" : post.likes,
        "shares" : post.shares,
        "comments" : post.comments,
        "created_at" : post.create_time
    }

posts = []

users = [
            {"name" : "maximus",
             "password" : "5413"
            },
            {"name" : "maxim",
             "password" : "5635"
            },
            {"name" : "max",
             "password" : "5135"
            }
        ]

comment_data = [
    {
        "name" : "max",
        "text" : "this is a demo comment"
    },
    {
        "name" : "kevin",
        "text" : "this is a demo comment"
    }
]


@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
            request_data = json.loads(request.body)
            for obj in users:
                 if request_data["name"].lower() == obj["name"].lower() and request_data["password"].lower() == obj["password"].lower():
                      return JsonResponse(data = {'message': 'found'}, status = 200)
            return JsonResponse(status=404, data = {'message': 'not found'})
    else:
        return JsonResponse({'error': 'Unsupported method or content type'}, status=400)
    

@csrf_exempt  
def create_post(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid request method")
    try:
        data = json.loads(request.body)
        title = data.get('title', None)
        body = data.get('body', None)
        comments = comment_data

        if not title or not body:
            return HttpResponseBadRequest("Missing required fields: title and body")
        posts.append(Post(title, body, comments))
        return JsonResponse({'message': 'Post created successfully'})

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON data")
    except Exception as e:
        return HttpResponseBadRequest(f"Error: {str(e)}")

@csrf_exempt  
def get_posts(request):
    if request.method != 'GET':
        return HttpResponseBadRequest("Invalid request method")

    data = []
    for post in posts:
        data.append(serialize_post(post))
    return JsonResponse(data, safe=False)