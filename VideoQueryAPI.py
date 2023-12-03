import requests

def query_videos(auth_token, fields, conditions, start_date, end_date, max_count=20, cursor=None, search_id=None, is_random=None):
    """
    Queries videos from the TikTok Researcher API.

    Parameters:
    auth_token (str): The client access token.
    fields (list): List of fields to retrieve from the Video Object.
    conditions (dict): The 'and', 'or', and 'not' conditions for filtering.
    start_date (str): The lower bound of video creation time in UTC.
    end_date (str): The upper bound of video creation time in UTC.
    max_count (int): The number of videos to return. Default is 20, max is 100.
    cursor (int): Retrieve video results starting from the specified index.
    search_id (str): The identifier for a cached search result.
    is_random (bool): Whether to return results in a random order.

    Returns:
    dict: A dictionary containing the response data.
    """

    endpoint = 'https://open.tiktokapis.com/v2/research/video/query/'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    
    payload = {
        'query': conditions,
        'start_date': start_date,
        'end_date': end_date,
        'max_count': max_count,
        'fields': ','.join(fields)
    }

    # Optional parameters
    if cursor is not None:
        payload['cursor'] = cursor
    if search_id is not None:
        payload['search_id'] = search_id
    if is_random is not None:
        payload['is_random'] = is_random

    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
