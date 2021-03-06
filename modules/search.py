import textwrap
from algoliasearch.search_client import SearchClient
import os
from modules.request import request
import requests
import modules.vars as horsy_vars
import json
from rich import print
from modules.http_status import handle

client = SearchClient.create(
    requests.get('https://raw.githubusercontent.com/horsy-ml/horsy/master/web_vars/search_app').json()['APP_ID'],
    requests.get('https://raw.githubusercontent.com/horsy-ml/horsy/master/web_vars/search_app').json()['API_KEY'])
index = client.init_index('packages')


def search(query, is_gui=False):
    res = index.search(query)['hits']
    ret_res = list()
    for i in res:
        if not is_gui:
            print(textwrap.shorten(f"{i['name']} by {i['authorName']} - {i['description']}",
                                   width=os.get_terminal_size().columns))
        else:
            ret_res.append(i['name'])

    return ret_res


def info(package, download_ui=None, UiDownloadWindow=None):
    r = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    r_code = handle(r.status_code)
    r = r.text
    r = json.loads(r)

    print(f"[bold]{r['name']}{'✅' if r['verified'] else ''} by {r['authorName']}[/]")
    print(f"{r['description']}")
    print(f"👍{r['likes']} | 👎{r['dislikes']}")
    if not r['verified']:
        print("This package is not verified by the horsy team. This means that it \n"
              "can be unstable or it can be malware. Most packages have unverified\n"
              "state, but use it at your own risk.")
    else:
        print("This package is [green]verified[/] by the horsy team! \n"
              "Keep in mind, developers can change the code after verification \n"
              "We [red]don't call you to trust this app[/], use it at your own risk \n"
              "but we recommend you more to install verified packages")
    if download_ui is not None:
        download_ui.logs_box.clear()
        UiDownloadWindow.show()
        download_ui.logs_box.append(f"{r['name']}{'✅' if r['verified'] else ''} by {r['authorName']}")
        download_ui.logs_box.append(f"{r['description']}")
        download_ui.logs_box.append(f"👍{r['likes']} | 👎{r['dislikes']}")
        download_ui.logs_box.append("")
        if not r['verified']:
            download_ui.logs_box.append("This package is not verified by the horsy team. This means that it \n"
                                        "can be unstable or it can be malware. Most packages have unverified\n"
                                        "state, but use it at your own risk.")
        else:
            download_ui.logs_box.append("This package is verified by the horsy team! \n"
                                        "Keep in mind, developers can change the code after verification \n"
                                        "We don't call you to trust this app, use it at your own risk \n"
                                        "but we recommend you more to install verified packages")
        return None
