#   Copyright 2017 Suzy M Stiegelmeyer 
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import twitter
import networkx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import json

# read in my secret keys
with open("keys.json",'r') as f:
    mykeys=json.load(f)

# establish connection with api
api = twitter.Api(consumer_key=mykeys['consumer_key'],
    consumer_secret=mykeys['consumer_secret'],
    access_token_key=mykeys['access_token_key'],
    access_token_secret=mykeys['access_token_secret'])

# get who I'm following
friends = api.GetFriends()
fto = [item.screen_name for item in friends]

# get who is following me
followers = api.GetFollowers()
ffrom = [item.screen_name for item in followers]

# make a directed graph
g = networkx.DiGraph()

for f in ffrom:
    if f in fto:
        g.add_edge("Elmos_Buddy",f)
        g.add_edge(f, "Elmos_Buddy")

# draw it
networkx.draw_networkx(g)
matplotlib.pyplot.savefig("blah.png")

# save it
networkx.write_gml(g,"blah.gml")




