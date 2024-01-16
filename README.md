# update-cloudflare-dns
by rob

# update your cloudflare dns A record using your ip
to use this script you must gain a cloudflare api token which is done [here](https://dash.cloudflare.com/profile/api-tokens).
add a file called .dotenv or replace your cloudflare api key in main.py.

this script works on linux and windows computers.
sorry mac users, i do not have a mac to test one with, i suppose you could always fork it.

# the usecase
this is mainly used for small-scale web servers, like home-based servers.
this makes setting the A record's ip easier (especially if you use VPNs or iCloud Private Relay like me.)

maybe this is only my scenario, but oh well it's here now.