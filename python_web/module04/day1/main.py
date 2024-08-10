import logging
from framework import GoITServer, GoITRequest, GoITResponce

logging.basicConfig(level="DEBUG")

api = GoITServer('0.0.0.0', 8080, static_folder="public")

# @api.post("/contact")
# def post_contact_handler(req: GoITRequest) -> GoITResponce:
#     logging.info(req.body)
#
#     return GoITResponce(
#         301,
#         {"Location": "/public/index.html"},
#         b""
#     )

if __name__ == "__main__":
    api.serve_forever()