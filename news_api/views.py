from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.
class NewsApi(APIView):
    API_KEY = "d6ca66e8649b465a8fc9fdaf25f57f5f"

    def get(self, req, id=None):
        country = req.GET.get("country")
        category = req.GET.get("category")

        if country:
            url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={self.API_KEY}"
        elif category:
            url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={self.API_KEY}"
        else:
            url = (
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.API_KEY}"
            )

        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        return Response({"articles": articles}, status=status.HTTP_200_OK)


class HealthCheck(APIView):
    def get(self, req):
        return Response({"msg": "status up"}, status=status.HTTP_200_OK)
