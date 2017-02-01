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
fto = set([item.screen_name for item in friends])

# get who is following me
followers = api.GetFollowers()
ffrom = set([item.screen_name for item in followers])

# common
both = fto & ffrom

# make a directed graph
g = networkx.DiGraph()

for f in both:
    g.add_edge("Elmos_Buddy",f)
    g.add_edge(f, "Elmos_Buddy")

networkx.draw_networkx(g)
matplotlib.pyplot.savefig("friend.png")
matplotlib.pyplot.close()

networkx.write_gml(g,"friends.gml")

g2 = networkx.DiGraph()
# tweets that were retweeted
rt=api.GetRetweetsOfMe()
for item in rt:
    # who retweeted the tweet
    lrt = api.GetRetweets(item.id)
    for tweets in lrt:
        if tweets.user.screen_name not in g2.node:
            g2.add_edge(tweets.user.screen_name, "Elmos_Buddy")
            if tweets.user.screen_name in both:
                g2.add_edge("Elmos_Buddy", tweets.user.screen_name)
        print(tweets.user.screen_name)

networkx.draw_networkx(g2)
matplotlib.pyplot.savefig("retweet.png")
networkx.write_gml(g2, "retweet.gml")





