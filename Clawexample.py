from ByteLightProject import claw                          # C L A W
subdomains_example = {                                     # u i d e
"/sub1": "<h1>Subdomain 1</h1>",                           # s g a b
"/sub2": "<h1>Subdomain 2</h1>",                           # t t p s
"/sub3": "<h1>Sub3</h1>"                                   # o w t e                 # Any amouth u want yet u have to also change the subdomain count.
}                                                          # m e a r
                                                           #   i b v
                                                           #   t l e
                                                           #   h e r
cd="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hi</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            font-size: 50px;
        }
    </style>
</head>
<body>
    <h1>Hi</h1>
</body>
</html>
"""


server = claw(
    html_option=True,
    html=cd,
    ip="127.0.0.1",
    port=8080,
    subdomain_option=True,
    subdomain_count=3,              # SUBDOMAIN COUNT HERE!
    subdomains=subdomains_example,
    return_server_logs_option=True
)

try:
    while True:pass
except KeyboardInterrupt:
    print("\nShutting down server...")
    server.shutdown()
    server.server_close()
