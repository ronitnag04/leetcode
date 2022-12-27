"""
To get cookies, headers, and json_data values:
1. Go to any question where you have made a successful submission, and click on the submissins tab
2. Right-click, inspect, and go to Network tab
3. Click reload
4. Click through all of the requests called graphql with the tab on Payload, until you find one with operationName: 'Submissions'
5. Right-click on the graphql request, Copy as cURL (bash), and paste into https://curlconverter.com/
6. Click on Python and copy the cookies, headers, and json_data values below
   Note: The cookies you get may look/be formatted differently, 
         I advise you copy the cookies, headers, and json_data values
         directly. The example values below are just to provide a reference 
         for what to look for.
"""


import requests
import json

cookies = {
    # My cookies dict looked something like this
    # ..... means random other cookies with weird names
    #
    # 'gr_user_id': ___
    # .....
    # '__stripe_mid'
    # .....
    # 'csrftoken': ___
    # .....
}

headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': f'""',
    'origin': 'https://leetcode.com',
    'referer': 'https://leetcode.com/problems/two-sum/submissions/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': '',
    'x-csrftoken': '',
    'x-newrelic-id': '',
}

json_data = {
    'operationName': 'Submissions',
    'variables': {
        'offset': 0,
        'limit': 20,
        'lastKey': None,
        'questionSlug': 'two-sum',
    },
    'query': 'query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n',
}

def getSubmissionDetails(questionSlug):
    json_data_copy = json_data.copy()
    json_data_copy['variables']['questionSlug'] = questionSlug


    response = requests.post('https://leetcode.com/graphql', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)

    raw_scores = data['data']['submissionList']['submissions']
    accepted_scores = [raw for raw in raw_scores if raw['statusDisplay'] == 'Accepted']

    best_score = min(accepted_scores, key= lambda score: int(score['runtime'].split(' ')[0]))
    runtime = best_score['runtime']
    memory = best_score['memory']
    best_score_url = 'https://leetcode.com/submissions/detail/' + best_score['id']

    return [runtime, memory, best_score_url]