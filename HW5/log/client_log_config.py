import logging

logging.basicConfig(
    filename="cl_app.log",
    format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
    level=logging.INFO
)

logger = logging.getLogger('basic')
