from os import mkdir, path
from shutil import rmtree
from urllib import robotparser
from pywebcopy import save_webpage
from validators import url
import var


class Eventos:

    def web_download(self):
        webpage_url = var.ui.lineEdit_url.text()
        if webpage_url != "" and url(webpage_url):
            var.ui.labelstatusbar.setText('DESCARGANDO...')
            download_folder = 'downloads/'
            if path.exists(download_folder):
                rmtree(download_folder)
            mkdir(download_folder)
            save_webpage(
                url=webpage_url,
                project_folder=download_folder,
                project_name=None,
                bypass_robots=True,
                debug=False,
                open_in_browser=True,
                delay=None,
                threaded=False,
            )
            var.ui.labelstatusbar.setText('DESCARGA COMPLETADA')
        else:
            var.ui.labelstatusbar.setText('INTRODUCE UNA URL')
