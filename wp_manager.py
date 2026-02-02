import requests

url = "http://localhost/mywordpress/wp-json/wp/v2/posts?per_page=3"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print("Τελευταία 3 άρθρα:\n")

    for post in posts:
        title = post["title"]["rendered"]
        print(f"- {title}")
else:
    print("Σφάλμα σύνδεσης με το WordPress API")