from apiclient.discovery import build


def youtube_api_helper(query, limit, key):
    DEVELOPER_KEY = key
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    try:
        service_object = build(
            API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY, cache_discovery=False
        )
        search_response = (
            service_object.search()
            .list(q=query, part="id, snippet", maxResults=limit)
            .execute()
        )
        response = search_response.get("items", [])

    except Exception:
        import traceback
        traceback.print_exc()
        return {}

    return response
