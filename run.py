from api import app
import config as cfg

if __name__ == '__main__':
    app.run(host=cfg.RESTAPI_HOST, port=cfg.RESTAPI_PORT, debug=False)